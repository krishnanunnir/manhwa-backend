from django.contrib.auth.models import User, Group
from django.db.models.query import QuerySet
from .models import Manhwa, ManhwaList
from rest_framework import serializers
import logging

logger = logging.getLogger(__name__)


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


class ManhwaListCreateSerializer(serializers.ModelSerializer):
    manhwas = serializers.SlugRelatedField(
        many=True, slug_field="slug", queryset=Manhwa.objects.all()
    )

    class Meta:
        model = ManhwaList
        fields = ("title", "identifier", "slug", "manhwas")
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}

    def create(self, validated_data):
        logger.debug(validated_data)
        manhwas_data = validated_data.pop("manhwas", [])
        manhwa_list = ManhwaList.objects.create(**validated_data)
        manhwa_list.save()
        for manhwas in manhwas_data:
            logger.debug(manhwas)
            manhwa_list.manhwas.add(manhwas)
        return manhwa_list


class ManhwaListListSerializer(serializers.ModelSerializer):
    manhwas = ManhwaSerializer(many=True, read_only=True)

    class Meta:
        model = ManhwaList
        fields = ("title", "identifier", "slug", "manhwas")
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
