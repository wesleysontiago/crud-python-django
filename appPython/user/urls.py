from django.urls import path, re_path
from user.admin import RegisterApi
from user.views import UserAPIView

urlpatterns = [
    path('user', UserAPIView.as_view()),
    re_path(r'user/(?P<pk>[0-9]+)$', UserAPIView.as_view()),
    path('register', RegisterApi.as_view()),
]