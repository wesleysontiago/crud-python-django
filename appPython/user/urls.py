from django.urls import path, re_path
from user.admin import RegisterApi
from user.views import UserAPIView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('openapi/', get_schema_view(
        title="Api Service",
        description="API developers hpoing to use our service"
    ), name='openapi-schema'),
    path('user', UserAPIView.as_view()),
    re_path(r'user/(?P<pk>[0-9]+)$', UserAPIView.as_view()),
    path('register', RegisterApi.as_view()),
]