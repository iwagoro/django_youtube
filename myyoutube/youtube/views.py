from django.shortcuts import render
from .models import Video,Comment
from .forms import UploadForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone


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

