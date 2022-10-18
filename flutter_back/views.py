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
    # data = json.loads(request.body.decode())
    data ="""{"timestamp":1665739965594,"webhookEvent":"jira:issue_updated","issue_event_type_name":"issue_updated","user":{"self":"https://trustyhost.atlassian.net/rest/api/2/user?accountId=5db82b13a766000da47cbfc7","accountId":"5db82b13a766000da47cbfc7","avatarUrls":{"48x48":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5db82b13a766000da47cbfc7/3e47ee5b-3c03-4fe8-848a-9b7f53cb0188/48","24x24":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5db82b13a766000da47cbfc7/3e47ee5b-3c03-4fe8-848a-9b7f53cb0188/24","16x16":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5db82b13a766000da47cbfc7/3e47ee5b-3c03-4fe8-848a-9b7f53cb0188/16","32x32":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5db82b13a766000da47cbfc7/3e47ee5b-3c03-4fe8-848a-9b7f53cb0188/32"},"displayName":"Kirill Poryadin","active":true,"timeZone":"Asia/Yerevan","accountType":"atlassian"},"issue":{"id":"148844","self":"https://trustyhost.atlassian.net/rest/api/2/14117","key":"EVA-49","fields":{"statuscategorychangedate":"2022-10-03T21:17:30.414+0400","customfield_10190":null,"customfield_10191":null,"customfield_10192":null,"customfield_10193":null,"customfield_10194":null,"customfield_10195":null,"customfield_10196":null,"customfield_10197":null,"customfield_10352":null,"fixVersions":[],"customfield_10198":null,"customfield_10199":null,"resolution":null,"customfield_10104":null,"lastViewed":"2022-10-14T13:32:27.751+0400","customfield_10181":null,"customfield_10182":null,"customfield_10183":null,"customfield_10184":null,"customfield_10185":null,"customfield_10186":null,"customfield_10187":null,"customfield_10100":"2022-10-13T16:03:32.379+0400","customfield_10188":null,"priority":{"self":"https://trustyhost.atlassian.net/rest/api/2/priority/3","iconUrl":"https://trustyhost.atlassian.net/images/icons/priorities/medium.svg","name":"Medium","id":"3"},"customfield_10101":null,"customfield_10189":null,"labels":["to_myth"],"timeestimate":0,"aggregatetimeoriginalestimate":118800,"versions":[],"issuelinks":[],"assignee":null,"status":{"self":"https://trustyhost.atlassian.net/rest/api/2/status/10370","iconUrl":"https://trustyhost.atlassian.net/images/icons/status_generic.gif","name":"To Do","id":"10370","statusCategory":{"self":"https://trustyhost.atlassian.net/rest/api/2/statuscategory/2","id":2,"key":"new","colorName":"blue-gray","name":"New"}},"components":[{"self":"https://trustyhost.atlassian.net/rest/api/2/component/10168","id":"10168","name":"test.com"},{"self":"https://trustyhost.atlassian.net/rest/api/2/component/10168","id":"10168","name":"marina"},{"self":"https://trustyhost.atlassian.net/rest/api/2/component/10168","id":"10168","name":"eva.com"}],"customfield_10170":null,"customfield_10171":null,"customfield_10172":null,"customfield_10173":[{"self":"https://trustyhost.atlassian.net/rest/api/2/customFieldOption/10166","value":"работает","id":"10166"}],"customfield_10174":null,"customfield_10175":null,"customfield_10176":null,"customfield_10177":null,"customfield_10178":null,"customfield_10179":null,"customfield_10203":[],"customfield_10204":null,"aggregatetimeestimate":0,"creator":{"self":"https://trustyhost.atlassian.net/rest/api/2/user?accountId=5db82b13a766000da47cbfc7","accountId":"5db82b13a766000da47cbfc7","avatarUrls":{"48x48":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5db82b13a766000da47cbfc7/3e47ee5b-3c03-4fe8-848a-9b7f53cb0188/48","24x24":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5db82b13a766000da47cbfc7/3e47ee5b-3c03-4fe8-848a-9b7f53cb0188/24","16x16":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5db82b13a766000da47cbfc7/3e47ee5b-3c03-4fe8-848a-9b7f53cb0188/16","32x32":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5db82b13a766000da47cbfc7/3e47ee5b-3c03-4fe8-848a-9b7f53cb0188/32"},"displayName":"Kirill Poryadin","active":true,"timeZone":"Asia/Yerevan","accountType":"atlassian"},"subtasks":[],"customfield_10163":null,"reporter":{"self":"https://trustyhost.atlassian.net/rest/api/2/user?accountId=5db82b13a766000da47cbfc7","accountId":"5db82b13a766000da47cbfc7","avatarUrls":{"48x48":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5db82b13a766000da47cbfc7/3e47ee5b-3c03-4fe8-848a-9b7f53cb0188/48","24x24":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5db82b13a766000da47cbfc7/3e47ee5b-3c03-4fe8-848a-9b7f53cb0188/24","16x16":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5db82b13a766000da47cbfc7/3e47ee5b-3c03-4fe8-848a-9b7f53cb0188/16","32x32":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5db82b13a766000da47cbfc7/3e47ee5b-3c03-4fe8-848a-9b7f53cb0188/32"},"displayName":"Kirill Poryadin","active":true,"timeZone":"Asia/Yerevan","accountType":"atlassian"},"customfield_10164":null,"aggregateprogress":{"progress":108000,"total":108000,"percent":100},"customfield_10200":null,"customfield_10201":null,"customfield_10168":null,"customfield_10202":null,"customfield_10169":null,"customfield_10159":null,"progress":{"progress":108000,"total":108000,"percent":100},"votes":{"self":"https://trustyhost.atlassian.net/rest/api/2/issue/EVA-49/votes","votes":0,"hasVoted":false},"issuetype":{"self":"https://trustyhost.atlassian.net/rest/api/2/issuetype/10146","id":"10146","description":"","iconUrl":"https://trustyhost.atlassian.net/images/icons/issuetypes/story.svg","name":"История","subtask":false,"hierarchyLevel":0},"timespent":108000,"customfield_10150":null,"customfield_10151":null,"project":{"self":"https://trustyhost.atlassian.net/rest/api/2/project/10112","id":"10112","key":"EVA","name":"Eva","projectTypeKey":"software","simplified":false,"avatarUrls":{"48x48":"https://trustyhost.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10400","24x24":"https://trustyhost.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10400?size=small","16x16":"https://trustyhost.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10400?size=xsmall","32x32":"https://trustyhost.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10400?size=medium"},"projectCategory":{"self":"https://trustyhost.atlassian.net/rest/api/2/projectCategory/10001","id":"10001","description":"Проекты, которые переносятся сюда, не должны быть видны никому кроме админов","name":"🗑️"}},"customfield_10152":null,"customfield_10153":null,"aggregatetimespent":108000,"customfield_10157":null,"customfield_10158":null,"customfield_10302":null,"customfield_10148":null,"customfield_10303":null,"customfield_10304":null,"customfield_10308":null,"resolutiondate":null,"workratio":90,"issuerestriction":{"issuerestrictions":{},"shouldDisplay":false},"watches":{"self":"https://trustyhost.atlassian.net/rest/api/2/issue/EVA-49/watchers","watchCount":2,"isWatching":true},"created":"2022-10-03T21:17:30.139+0400","customfield_10140":null,"customfield_10141":null,"customfield_10020":null,"customfield_10142":null,"customfield_10021":null,"customfield_10143":null,"customfield_10144":null,"customfield_10145":null,"customfield_10300":null,"customfield_10147":null,"customfield_10301":null,"customfield_10016":null,"customfield_10017":null,"customfield_10138":null,"customfield_10018":{"hasEpicLinkFieldDependency":false,"showField":false,"nonEditableReason":{"reason":"PLUGIN_LICENSE_ERROR","message":"Ссылка на родителя доступна только пользователям Jira Premium."}},"customfield_10139":[],"customfield_10019":"0|i00mib:","updated":"2022-10-14T13:32:45.576+0400","customfield_10370":null,"timeoriginalestimate":118800,"customfield_10371":null,"description":"Flutter task description. FF. ААА ggg","customfield_10372":null,"customfield_10010":null,"customfield_10014":null,"customfield_10015":"2022-10-19","timetracking":{"originalEstimate":"40ч","remainingEstimate":"0ч","timeSpent":"30ч","originalEstimateSeconds":118800,"remainingEstimateSeconds":0,"timeSpentSeconds":108000},"customfield_10005":null,"customfield_10126":null,"customfield_10006":null,"customfield_10369":null,"security":{"self":"https://trustyhost.atlassian.net/rest/api/2/securitylevel/10101","id":"10101","description":"","name":"th-self"},"customfield_10007":null,"customfield_10008":null,"attachment":[],"customfield_10009":null,"summary":"Test flutter","customfield_10000":"{}","customfield_10001":null,"customfield_10123":null,"customfield_10002":null,"customfield_10003":null,"customfield_10124":null,"customfield_10125":null,"customfield_10004":null,"environment":null,"customfield_10118":null,"customfield_10119":null,"duedate":"2022-10-11"}},"changelog":{"id":"91190","items":[{"field":"description","fieldtype":"jira","fieldId":"description","from":null,"fromString":"Flutter task description. FF. ААА","to":null,"toString":"Flutter task description. FF. ААА ggg"}]}}"""
    # jsonStr = json.dumps(data)
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


class TaskListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # tasks = Task.objects.all()
        user = self.request.user
        tasks = Task.objects.filter(components__components__username = user)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data)


class ComponentListView(APIView):
    def get(self, request):
        component = Component.objects.all()
        serializer = ComponentListSerializer(component, many=True)
        return Response(serializer.data)