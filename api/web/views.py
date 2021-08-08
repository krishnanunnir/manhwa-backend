from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import ManhwaListSerialier, ManhwaSerializer
from .models import Manhwa, ManhwaList

# Create your views here.


class ManhwaViewSet(viewsets.ModelViewSet):
    queryset = Manhwa.objects.filter(verified=True).order_by("created_at")
    serializer_class = ManhwaSerializer
    lookup_field = "slug"


class ManhwaListViewSet(viewsets.ModelViewSet):
    queryset = ManhwaList.objects.filter()
    serializer_class = ManhwaListSerialier
    lookup_field = "slug"
