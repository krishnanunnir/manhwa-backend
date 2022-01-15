from django.contrib.auth.models import User
from django.db.models import query
from rest_framework import viewsets
from .serializers import (
    ManhwaCreateSerializer,
    ManhwaSerializer,
    ManhwaListCreateSerializer,
    ManhwaListListSerializer,
    TagsSerializer,
)
from .models import Manhwa, ManhwaList, Tags
from django.db.models import Q

# Create your views here.


class ManhwaViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "create":
            return ManhwaCreateSerializer
        else:
            return ManhwaSerializer

    def get_queryset(self):
        queryset = self.queryset
        tag_query = self.request.query_params.get("tag")
        search_query = self.request.query_params.get("search")
        if tag_query:
            queryset = queryset.filter(tags__slug__in=tag_query.split(","))
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
                | Q(alternate_names__icontains=search_query)
            )
        return queryset

    queryset = Manhwa.objects.filter(
        verification_status=Manhwa.VERIFICATION_STATUS_VERIFIED
    ).order_by("created_at")
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
    queryset = Tags.objects.all().order_by("name")
    pagination_class = None
    serializer_class = TagsSerializer
    lookup_field = "slug"
    http_method_names = ["get"]
