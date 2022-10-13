from django.contrib import admin
from django.urls import path, include, re_path
from .views import TaskListView, TaskDetailView, ComponentListView

urlpatterns = [
    # path('', marina),
    path('tasks/', TaskListView.as_view()),
    path('tasks/<int:pk>', TaskDetailView.as_view()),
    path('components/', ComponentListView.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
