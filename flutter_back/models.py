from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


from .managers import CustomUserManager


class Component(models.Model):
    component_name = models.CharField(max_length = 1000, verbose_name = "Название компонента")

    def __str__(self):
        return "%s" % (self.component_name)

    class Meta:
         verbose_name = "Компонент"
         verbose_name_plural = "Компоненты"


class Task(models.Model):
    jira_id = models.IntegerField(max_length = 500, verbose_name = "ID в Jira", null=True)
    name = models.CharField(max_length = 1000, verbose_name = "Название задачи", null=True)
    deadline = models.CharField(max_length = 1000, verbose_name = "Дата сдачи", null=True)
    status_name = models.CharField(max_length = 100, verbose_name = "Имя статуса", null=True)
    timeSpent = models.CharField(max_length = 1000, verbose_name = "Затраченное время", null=True)
    priority = models.CharField(max_length = 1000, verbose_name = "Приоритет", null=True)
    startDate = models.CharField(max_length = 1000, verbose_name = "Дата начала", null=True)
    originalEstimate = models.CharField(max_length = 1000, verbose_name = "Исходная оценка времени", null=True)
    components = models.ManyToManyField(Component, verbose_name = "Связанные компоненты", related_name = "taskComp")

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
         verbose_name = "Задача"
         verbose_name_plural = "Задачи"


# class TaskComp(models.Model):
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     component = models.ForeignKey(Component, on_delete=models.CASCADE)


class CustomUser(AbstractUser):
    components = models.ManyToManyField(Component, verbose_name = "Связанные компоненты", related_name="components")

    # objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'is_active', 'is_staff']

    def __str__(self):
        return self.username
