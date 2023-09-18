from django.shortcuts import render
from .models import Video,Comment
from .forms import UploadForm
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse
import json
from django.http import JsonResponse


def home(request):
    videos = Video.objects.all()
    return render(request,'youtube/home.html',{'videos':videos})


from django.shortcuts import render

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        print("upload")
        if form.is_valid():
            print("form is valid")
            video = form.save(commit=False)
            video.published_at = timezone.now()
            video.save()
            return redirect('home')
    else:
        form = UploadForm()
    return render(request, 'youtube/upload.html', {'form': form})


def video_detail(request,pk):
    selectedVideo = get_object_or_404(Video,pk=pk)
    videos = Video.objects.all()
    comments = Comment.objects.filter(video=selectedVideo)
    return render(request,'youtube/video_detail.html',{'selectedVideo':selectedVideo,'videos':videos,'comments':comments})

def comment(request):
    comment = request.POST.get('comment')
    video_id = request.POST.get('video_id')
    publish_at = timezone.now()
    if(comment != None and video_id != None):
        new_comment = Comment(video_id=video_id,text=comment,published_at=publish_at)
        new_comment.save()
    return JsonResponse({'comment':comment})
