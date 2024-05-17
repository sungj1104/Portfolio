from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User


# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField("Todo의 제목", max_length=100)
    description = models.TextField("Todo에 대한 설명", null=True)
    created = models.DateTimeField("Todo 생성일자", auto_now_add = True)
    complete = models.BooleanField("Todo 완료 여부", default = False)
    important = models.BooleanField("Todo 중요 여부", default = False)

