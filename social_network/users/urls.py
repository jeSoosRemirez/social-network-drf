from django.urls import path
from users.views import RegisterUserAPIView, LoginUserAPIView, RetrieveUpdateUserAPI
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('login/', LoginUserAPIView.as_view(), name='login'),
    path('update/', RetrieveUpdateUserAPI.as_view(), name='update'),
])
