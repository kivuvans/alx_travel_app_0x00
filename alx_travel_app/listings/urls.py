from django.urls import path
from django.http import JsonResponse

def sample_view(request):
    return JsonResponse({"message": "Welcome to ALX Travel Listings API"})

urlpatterns = [
    path('', sample_view),
]
