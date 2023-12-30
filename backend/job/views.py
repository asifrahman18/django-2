from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer

# Create your views here.

@api_view(['GET'])
def getAllJobs(request):
    
    jobs = Job.objects.all()
    
    serializer = JobSerializer(jobs, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def getJob(request, pk):
    
    job = Job.objects.get(id=pk)
    
    serializer = JobSerializer(job, many=False)
    
    return Response(serializer.data)