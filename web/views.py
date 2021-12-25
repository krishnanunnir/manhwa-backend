from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import (
    ManhwaCreateSerializer,
    ManhwaSerializer,
    ManhwaListCreateSerializer,
    ManhwaListListSerializer,
    TagsSerializer,
)
from .models import Manhwa, ManhwaList, Tags

# Create your views here.


class ManhwaViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "create":
            return ManhwaCreateSerializer
        else:
            return ManhwaSerializer

    queryset = Manhwa.objects.filter(verified=True).order_by("created_at")
    lookup_field = "slug"
    http_method_names = ["get", "post"]


class ManhwaListViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "create":
            return ManhwaListCreateSerializer
        else:
            return ManhwaListListSerializer

    queryset = ManhwaList.objects.filter()
    lookup_field = "slug"
    http_method_names = ["get", "post"]


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    pagination_class = None
    serializer_class = TagsSerializer
    lookup_field = "slug"
    http_method_names = ["get"]
