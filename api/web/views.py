from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import ManhwaSerializer
from .models import Manhwa

# Create your views here.


class ManhwaViewSet(viewsets.ModelViewSet):
    queryset = Manhwa.objects.filter(verified=True).order_by("created_at")
    serializer_class = ManhwaSerializer
    lookup_field = "slug"
