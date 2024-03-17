from django.contrib import admin
from django.urls import path
from api.views import ProjectAPI

urlpatterns = [
    path('project/',
         ProjectAPI.as_view(),
         name='project'
    ),
    path('project/<int:pk>/',
         ProjectAPI.as_view(),
         name='project'
    ),
]
