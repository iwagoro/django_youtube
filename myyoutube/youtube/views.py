from django.shortcuts import render
from .models import Video,Comment
from .forms import UploadForm
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse



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
    if request.method == 'POST':
        print("post")
        form = CommentForm(request.POST)
        if form.is_valid():
            print("form is valid")
            comment = form.save(commit=False)
            comment.video = selectedVideo
            comment.published_at = timezone.now()
            comment.save()
            return redirect('video_detail',pk=pk)
    else:
        form = CommentForm()
    return render(request,'youtube/video_detail.html',{'form':form,'selectedVideo':selectedVideo,'videos':videos,'comments':comments})
