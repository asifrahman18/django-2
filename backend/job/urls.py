from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from . import views
from job.views import AllJobsView, AddJobView, UpdateJobView, JobDetailView, DeleteJobView, TopicStatView, RegisterView
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
    path('user/token/verify/', TokenVerifyView.as_view(), name='token_refresh'),
]