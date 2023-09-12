from django.shortcuts import render
from .models import Video,Comment

# Create your views here.
def home(request):
    videos = Video.objects.all()
    return render(request,'youtube/home.html',{'videos':videos})