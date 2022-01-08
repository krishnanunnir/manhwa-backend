from django.contrib.auth.models import User, Group
from django.db.models.query import QuerySet
from .models import Manhwa, ManhwaList, Tags
from rest_framework import serializers
import logging

logger = logging.getLogger(__name__)


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ("name", "slug")
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}


class ManhwaSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)

    class Meta:
        model = Manhwa
        fields = (
            "title",
            "author",
            "slug",
            "type",
            "description",
            "status",
            "cover_image",
            "tags",
        )
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}


class ManhwaCreateSerializer(serializers.ModelSerializer):
    tags = serializers.CharField(max_length=2000)

    class Meta:
        model = Manhwa
        fields = (
            "title",
            "author",
            "slug",
            "description",
            "type",
            "status",
            "cover_image",
            "tags",
        )
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}

    def create(self, validated_data):
        tags_list = validated_data.pop("tags", []).split(",")
        manhwa = Manhwa.objects.create(**validated_data)
        for tag in tags_list:
            manhwa.tags.add(Tags.objects.get(slug=tag))
        manhwa.save()
        return manhwa


class ManhwaListCreateSerializer(serializers.ModelSerializer):
    manhwas = serializers.SlugRelatedField(
        many=True, slug_field="slug", queryset=Manhwa.objects.all()
    )

    class Meta:
        model = ManhwaList
        fields = ("title", "identifier", "slug", "manhwas", "description")
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
        fields = ("title", "identifier", "slug", "manhwas", "description")
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
