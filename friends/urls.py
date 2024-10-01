from django.urls import path
from friends.views import list_friends, list_best_friends, list_recommended_friends


urlpatterns = [
    path('list_friends/', list_friends),
    path('list_best_friends/', list_best_friends),
    path('list_recommended_friends/', list_recommended_friends),

]