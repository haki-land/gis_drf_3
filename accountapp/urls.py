from django.urls import path
from rest_framework.authtoken import views

from accountapp.views import hello_world, hello_world_template, AccountCreateTemplate, AccountCreateAPIView, \
    AccountLoginTemplate

app_name = 'accountapp'

urlpatterns = [
    path('hello_world_template/', hello_world_template, name='hello_world_template'),
    path('hello_world/', hello_world, name='hello_world'),

    path('login_template/', AccountLoginTemplate, name='login_template'),
    path('login/', views.obtain_auth_token, name='login'),

    path('create_template/', AccountCreateTemplate, name='create_template'),
    path('create/', AccountCreateAPIView.as_view(), name='create'),

]
