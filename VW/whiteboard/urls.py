from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.before_meeting, name='before_meeting'),
    path('create_agenda/', views.create_agenda, name='create_agenda')
]
urlpatterns += static('documents', document_root=".")

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()