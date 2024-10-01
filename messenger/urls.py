from django.urls import path
from messenger.views import messages, create_group, write_friend

urlpatterns = [
    path('', messages),
    path('create_group/', create_group),
    path('write_friend/', write_friend),
]