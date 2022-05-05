from django.urls import path
from user import views

urlpatterns = [
    path('user', views.user_list),
    path(r'user/(?P<id>[0-9]+)$', views.user_detail)
]