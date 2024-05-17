from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        pass
    
    else:
        pass
    
    #return render(request,"index.html")
