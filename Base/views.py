from django.shortcuts import render 

def base_view(request): 
    return render(request, "home_base.html") 