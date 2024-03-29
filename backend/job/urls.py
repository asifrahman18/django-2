from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from . import views
from job.views import AllJobsView, AddJobView, UpdateJobView, JobDetailView, DeleteJobView, TopicStatView, RegisterView, CurrentUserView, CompanyCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

router = DefaultRouter()
#router.register(r'jobs', JobsViewSet, basename='jobs')

urlpatterns = [

    path('', include(router.urls)),
    path('jobs/', AllJobsView.as_view(), name='all_jobs'),
    path('jobs/<str:pk>/', JobDetailView.as_view(), name='job'),
    
    #path('jobs/<str:pk>/update/', UpdateJobView, name='update_job'),
    
    path('jobs/<str:pk>/update/', UpdateJobView.as_view(), name='update_job'),
    path('jobs/<str:pk>/delete', DeleteJobView.as_view(), name='delete_job'),
    path('jobs/stat/<str:topic>/', TopicStatView.as_view(), name='topic_stat'),
    path('jobs/add/', AddJobView.as_view(), name='add-job'),
    
    
    path('user/register/', RegisterView.as_view(), name='register'),
    
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('user/me/', CurrentUserView.as_view(), name='current_user'),
    
    path('user/<int:user_id>/register/', CompanyCreateView.as_view(), name='register_company'),

    
    
    
    
    
    
    #todo
    #show company(s) under an user
    path('user/<int:user_id>/copmpany/', CompanyView.as_view(), name='register_company'),
    
    #create job from company
    path('user/<int:user_id>/company/<int:comp_id>/addjob/', AddJobView.as_view(), name='register_company'),

]