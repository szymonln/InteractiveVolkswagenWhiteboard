from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.before_meeting, name='before_meeting'),
    path('create_agenda/', views.create_agenda, name='create_agenda'),
    path('create_area/', views.create_area, name='create_area'),
    path('create_select_whiteoard', views.create_select_whiteboard, name='create_select_whiteboard'),
    path('add_files_to_whiteboard', views.add_files_to_whiteboard, name='add_files_to_whiteboard'),
    path('meeting', views.meeting, name='meeting')
]
urlpatterns += static('documents', document_root=".")

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()