from django.contrib.auth.models import User, Group
from .models import Manhwa, ManhwaList
from rest_framework import serializers


class ManhwaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manhwa
        fields = (
            "title",
            "author",
            "slug",
            "description",
            "status",
            "cover_image",
            "tags",
        )
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}


class ManhwaListSerialier(serializers.ModelSerializer):
    manhwas = serializers.SlugRelatedField(many=True, slug_field="slug", read_only=True)

    class Meta:
        model = ManhwaList
        fields = ("title", "identifier", "slug", "manhwas")
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
