from django.shortcuts import render


def index(request):
    return render(request,'Kids/index.html')
# Create your views here.
