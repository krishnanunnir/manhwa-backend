from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import (
    ManhwaSerializer,
    ManhwaListCreateSerialier,
    ManhwaListListSerialier,
)
from .models import Manhwa, ManhwaList

# Create your views here.


class ManhwaViewSet(viewsets.ModelViewSet):
    queryset = Manhwa.objects.filter(verified=True).order_by("created_at")
    serializer_class = ManhwaSerializer
    lookup_field = "slug"


class ManhwaListViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "create":
            return ManhwaListCreateSerialier
        else:
            return ManhwaListListSerialier

    queryset = ManhwaList.objects.filter()
    lookup_field = "slug"
