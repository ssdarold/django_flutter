from rest_framework import serializers
from .models import Task, Component




class ComponentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Component
        fields = ("id", "component_name")


class TaskListSerializer(serializers.ModelSerializer):

    components = ComponentListSerializer(many=True, read_only=True)


    class Meta:
        model = Task
        fields = ("id", "jira_id", "name", "deadline", "status_id", "components")


class TaskDetailSerializer(serializers.ModelSerializer):
    components = ComponentListSerializer(many=True, read_only=True)


    class Meta:
        model = Task
        fields = ("id", "jira_id", "name", "deadline", "status_id", "components")