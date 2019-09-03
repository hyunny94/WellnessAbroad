from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'authentication'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_profile', views.create_profile, name='create_profile'),
    path('profile', views.view_profile, name='view_profile'),
    path('edit_profile_name', views.edit_profile, {'item': 'name'}, name='edit_profile_name'),
    path('edit_profile_image', views.edit_profile, {'item': 'image'}, name='edit_profile_image'),
    path('edit_profile_email', views.edit_profile, {'item': 'email'}, name='edit_profile_email'),
    path('edit_profile_age', views.edit_profile, {'item': 'age'}, name='edit_profile_age'),
    path('edit_profile_gender', views.edit_profile, {'item': 'gender'}, name='edit_profile_gender'),
    path('edit_profile_interest', views.edit_profile, {'item': 'interest'}, name='edit_profile_interest'),
    path('about', views.about, name='about')
]
