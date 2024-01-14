from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer, SignUpSerializer, UserSerializer
import json
from .forms import JobForm
from rest_framework import viewsets

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from django.views.generic.edit import CreateView

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

from django.shortcuts import get_object_or_404
from django.db.models import Count, Max, Min, Avg


from rest_framework.views import APIView

from rest_framework import status

from .filters import JobsFilter

# Create your views here.


# class JobsViewSet(viewsets.ModelViewSet):
#     # model = Job
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer


class AllJobsView(APIView):
    def get(self, request, format=None):
        filterset = JobsFilter(request.GET, queryset=Job.objects.all().order_by('id'))
        serializer = JobSerializer(filterset.qs, many=True)
        return Response(serializer.data)


class JobDetailView(APIView):

    def get(self, request, pk):
        try: 
            job = Job.objects.get(id=pk) 
            serializer = JobSerializer(job) 
            return Response(serializer.data)
        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



class AddJobView(APIView):
    def post(self, request):
        # Get data from request
        title = request.data.get('title') 
        description = request.data.get('description')
        email = request.data.get('email')
        location = request.data.get('location')
        job_type = request.data.get('jobType')
        qualification = request.data.get('qualification')
        salary = request.data.get('salary') 
        openings = request.data.get('openings')
        company = request.data.get('company')
        

        job = Job() 
        job.title = title
        job.description = description
        job.email = email
        job.location = location
        job.jobType = job_type
        job.qualification = qualification
        job.salary = salary
        job.openings = openings 
        job.company = company
        job.user = request.user
        
        # Save to db
        job.save()
        
        return Response(status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def UpdateJobView(request, pk):
    
    job = Job.objects.get(id=pk)
    
    job.title = request.data['title']
    job.description = request.data['description']
    job.email = request.data['email']
    job.location = request.data['location']
    job.jobType = request.data['jobType']
    job.qualification = request.data['qualification']
    job.salary = request.data['salary']
    job.openings = request.data['openings']
    job.expiresAt = request.data['expiresAt']
    
    job.save()
    
    serializer = JobSerializer(job, many=False)
    
    return Response(serializer.data)




class DeleteJobView(APIView):
    def delete(self, request, pk, format=None):
        job = get_object_or_404(Job, pk=pk)
        job.delete()
        return Response({'message': 'Job deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



class TopicStatView(APIView):
    def get(self, request, topic, format=None):
        args = {'title__icontains': topic}
        jobs = Job.objects.filter(**args)

        if len(jobs) == 0:
            return Response({'message': 'No jobs found!'}, status=status.HTTP_404_NOT_FOUND)

        stats = jobs.aggregate(
            count=Count('id'),
            avg_salary=Avg('salary'),
            min_salary=Min('salary'),
            max_salary=Max('salary'),
        )

        return Response(stats)




class RegisterView(APIView):
    def post(self, request, format=None):
        data = request.data
        user_serializer = SignUpSerializer(data=data)

        if user_serializer.is_valid():
            if not User.objects.filter(email=data['email']).exists():
                user = User.objects.create(
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email'],
                    password=make_password(data['password']),
                    username=data['email']
                )
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'User with this email already exists!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def register(request):
#     data = request.data
    
#     user = SignUpSerializer(data=data)
    
#     if user.is_valid:
#         if not User.objects.filter(email=data['email']).exists():
#             user = User.objects.create(
#                 first_name = data['first_name'],
#                 last_name = data['last_name'],
#                 email = data['email'],
#                 password = make_password(data['password']),
#                 username = data['email']
#             )
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response({'message': 'User with this email already exists!'}, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response(user.errors)


# @api_view(['GET'])
# def getTopicStat(request, topic):
    
#     args = {'topic__icontains': topic}
#     jobs = Job.objects.filter(**args)
    
    
#     if len(jobs) == 0:
#         return Response({'message': 'No jobs found!'}, status=status.HTTP_404_NOT_FOUND)
    
#     stats = jobs.aggregrate(
#         count=Count('id'),
#         avg_salary=Avg('salary'),
#         min_salary=Min('salary'),
#         max_salary=Max('salary'),
#     )
    
#     return Response(stats)



# @api_view(['DELETE'])
# def DeleteJob(request, pk):
    
#     job = get_object_or_404(Job, pk=pk)
    
#     job.delete()
    
#     return Response({'message': 'Job deleted successfully!'})











#------------------------------------------------------------------



# class UpdateJobView(APIView):
#     def get_object(self, pk):
#         try:
#             return Job.objects.get(pk=pk)
#         except Job.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         job = self.get_object(pk)
#         serializer = JobSerializer(job)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         try:
#             job = Job.objects.get(pk=pk)
#         except Job.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND) 
        
#         serializer = JobSerializer(job, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET'])
# def getAllJobs(request):
    
#     filterset = JobsFilter(request.GET, queryset=Job.objects.all().order_by('id'))
    
#     serializer = JobSerializer(filterset.qs, many=True)
    
#     return Response(serializer.data)


# @api_view(['GET'])
# def getJob(request, pk):
    
#     job = Job.objects.get(id=pk)
    
#     serializer = JobSerializer(job, many=False)
    
#     return Response(serializer.data)




# def addJobs(request):
#     if request.method == "POST":
#         form = JobForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = JobForm()


# @api_view(['POST'])
# def addJob(request):
    
#     data = request.data
    
#     job = Job.objects.create(**data)
    
#     serializer = JobSerializer(job, many=False)
    
#     return Response(serializer.data)
