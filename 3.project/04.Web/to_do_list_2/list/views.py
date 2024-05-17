from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from list import models
# Create your views here.

def index(request):
    text = models.Create.objects.all()
    content = {"text" : text}
    return render(request, "list/index.html", content)

def create(request):
    input = request.POST['create']
    new_content = models.Create(content=input)
    new_content.save()
    return HttpResponseRedirect(reverse("list:index"))