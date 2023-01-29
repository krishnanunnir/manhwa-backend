from django.contrib.postgres.search import SearchVector
from rest_framework import viewsets

from .models import Blog, Manhwa, ManhwaList, Tags
from .serializers import (BlogSerializer, ManhwaCreateSerializer,
                          ManhwaListCreateSerializer, ManhwaListListSerializer,
                          ManhwaSerializer, TagsSerializer)

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
            queryset = queryset.annotate(
                search=SearchVector("title", "alternate_names", "description")
            ).filter(search=search_query)

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


class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by("id")
    serializer_class = BlogSerializer
    lookup_field = "slug"
    http_method_names = ["get"]
