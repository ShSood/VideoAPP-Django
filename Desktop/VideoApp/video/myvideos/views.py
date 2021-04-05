from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Video
def index(request):
    video_list =Video.objects.all()
    print("Video List")
    print(video_list)
    videos = Paginator(video_list,3)
    print("paginated List")
    print(videos)
    grouped_videos=[]
    for page in videos.page_range:
        page_objects=videos.page(page).object_list
        print("page Objects",page_objects)
        grouped_videos.append(page_objects)
    print("GROUPED VIDEOS",grouped_videos)
    context={'videos':videos, 'grouped_videos': grouped_videos}
    return render(request, 'myvideos/index.html',context)

def video(request,video_id):
    the_video = Video.objects.get(pk=video_id)
    context ={"the_video": the_video}
    return render(request, 'myvideos/video.html', context)
