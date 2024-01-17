from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from . import views
from job.views import AllJobsView, AddJobView, UpdateJobView, JobDetailView, DeleteJobView, TopicStatView, RegisterView, CurrentUserView, CompanyCreateView, CompanyDetailView, AllCompaniesView


from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

router = DefaultRouter()
#router.register(r'jobs', JobsViewSet, basename='jobs')

urlpatterns = [

    path('', include(router.urls)),
    
    #all jobs listed
    path('jobs/', AllJobsView.as_view(), name='all_jobs'),
    
    #particular job details
    path('jobs/<str:pk>/', JobDetailView.as_view(), name='job'),

    
    #delete particular job
    path('jobs/<str:pk>/delete', DeleteJobView.as_view(), name='delete_job'),
    
    #see stats of particular job topic
    path('jobs/stat/<str:topic>/', TopicStatView.as_view(), name='topic_stat'),
    
    
    #register user
    path('user/register/', RegisterView.as_view(), name='register'),
    
    
    #obtain tokens using username, password
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    
    
    
    path('user/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('user/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    
    
    #see logged in user informations
    path('user/me/', CurrentUserView.as_view(), name='current_user'),
    
    
    #create company from user; ID number of user has to be passed
    path('user/me/register_company/', CompanyCreateView.as_view(), name='register_company'),
    
    
    
    #list all companies
    path('companies/', AllCompaniesView.as_view(), name='all_companies'),
    
    
    
    #view all company of that user (todo)
    path('user/me/company/', CompanyDetailView.as_view(), name='register_company'),

]