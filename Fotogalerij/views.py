from django.shortcuts import render 
from .models import MyModel

def fotogalerij(request):
    mymodels = MyModel.objects.all()
    return render(request, 'fotogalerij_base.html', {'mymodels': mymodels})
