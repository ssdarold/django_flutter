from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Task, Component
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskListSerializer, TaskDetailSerializer, ComponentListSerializer
from rest_framework.permissions import IsAuthenticated
import json




# Обработчик данных от Jira
# class GetJsonData(request):
#     data = json.loads(request.body.decode())
#     print(data)

def GetJsonData(request):
    data = json.loads(request.body.decode())
    jsonStr = json.dumps(data)
    result = json.loads(data)
    timeSpent = result['issue']['fields']['timetracking']['timeSpent'] # Затраченное на задачу время
    priority = result['issue']['fields']['priority']['name'] # Приоритет
    startDate = result['issue']['fields']['customfield_10015'] # Дата начала
    originalEstimate = result['issue']['fields']['timetracking']['originalEstimate'] # Исходная оценка времени
    jiraID = result['issue']['id'] # ID задачи в Джире
    taskName = result['issue']['fields']['summary'] # Имя задачи
    deadline = result['issue']['fields']['duedate'] # Срок сдачи
    status = result['issue']['fields']['status']['name'] # Имя статуса задачи
    components = result['issue']['fields']['components'] # Имя статуса задачи
    comp_res = []
    for comp in components:
        comp_res.append(comp['name'])

    Task.objects.update_or_create(
    jira_id=jiraID, 
    defaults={'jira_id': jiraID, 'name': taskName, 'deadline': deadline, 'status_name': status, 'timeSpent': timeSpent, 'priority': priority, 'startDate': startDate, 'originalEstimate': originalEstimate},
)

    currentTask = Task.objects.get(jira_id = jiraID)

    #Добавление компонентов
    for onecomp in comp_res:
        currentComp = Component.objects.filter(component_name=onecomp)
        if currentComp.exists():
            getComp = Component.objects.get(component_name=onecomp)
            compQuerySet = Component.objects.filter(taskComp__jira_id = jiraID)
            compCount = compQuerySet.filter(component_name=onecomp).count()
            if compCount == 0:
                currentTask.components.add(getComp)
            finalres = "Другое чето"
        else:
            newComp = Component.objects.create(component_name=onecomp)
            newCompQuerySet = Component.objects.filter(taskComp__jira_id = jiraID)
            newCompCount = newCompQuerySet.filter(component_name=onecomp).count()
            if newCompCount == 0:
                currentTask.components.add(newComp)
                finalres = "Успех!"
        

    #Удаление компонентов
    oldComps = Component.objects.filter(taskComp__jira_id = jiraID) #Получаем имена всех компонентов, связанных с данной задачей
    for oldcomp in oldComps:
        if oldcomp not in comp_res:
            pass
            finalres = "Снесли"
        else:
            compForDelete = Component.objects.get(component_name=oldcomp)
            currentTask.components.remove(compForDelete)
            finalres = oldcomp

    return HttpResponse(finalres)

# Вывод списка задач
class TaskListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # tasks = Task.objects.all()
        user = self.request.user
        tasks = Task.objects.filter(components__components__username = user)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)

# Вывод отдельной задачи
class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data)

# Вывод списка компонентов (проектов, с которыми связаны задачи)
class ComponentListView(APIView):
    def get(self, request):
        component = Component.objects.all()
        serializer = ComponentListSerializer(component, many=True)
        return Response(serializer.data)
