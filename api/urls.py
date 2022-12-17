from django.urls import path 
from .views import memeview

urlpatterns = [
    path("", memeview.as_view(), name="memeview")
]
