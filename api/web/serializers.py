from django.contrib.auth.models import User, Group
from .models import Manhwa
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
