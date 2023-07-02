# import repath
from django.urls import path
from rest_framework import routers

from .views import ManhwaTemplateView

# match all urls to manhwa/ to the view ManhwaTemplateView


urlpatterns = [
    path("", ManhwaTemplateView.as_view(), name="index"),
    path("manhwa/<slug:slug>", ManhwaTemplateView.as_view(), name="manhwa"),
]
