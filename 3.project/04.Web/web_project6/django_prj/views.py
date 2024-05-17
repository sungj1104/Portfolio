from django.shortcuts import render, redirect

def index(request):
    return render("single_pages:single_pages")
