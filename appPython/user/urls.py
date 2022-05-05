from django.urls import path, re_path
from user import views

urlpatterns = [
    path('user', views.user_list),
    re_path(r'user/(?P<pk>[0-9]+)$', views.user_detail)
]