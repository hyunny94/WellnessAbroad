from django.urls import path

from . import views

app_name = 'event'
urlpatterns = [
    path('index', views.event_index, name='event_index'),
    path('create_event', views.create_event, name='create_event'),
    path('update_participants/<int:event_id>', views.update_participants, name='update_participants')
] 
