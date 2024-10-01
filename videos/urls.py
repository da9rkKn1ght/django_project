from django.urls import path
from videos.views import list_your_videos, list_recommended_videos, load_video

urlpatterns = [
    path('list_your_videos/', list_your_videos),
    path('list_recommended_videos/', list_recommended_videos),
    path('load_video/', load_video),
]