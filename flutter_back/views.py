from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, Component
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskListSerializer, TaskDetailSerializer, ComponentListSerializer
from rest_framework.permissions import IsAuthenticated



# def marina(request):
#     tasks = Tasks.objects.all()
#     components = Components.objects.all()
#     return render(request, "marina.html", {"tasks": tasks})


class TaskListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # tasks = Task.objects.all()
        user = self.request.user
        tasks = Task.objects.filter(components__components__username = user)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskDetailView(APIView):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data)


class ComponentListView(APIView):
    def get(self, request):
        component = Component.objects.all()
        serializer = ComponentListSerializer(component, many=True)
        return Response(serializer.data)