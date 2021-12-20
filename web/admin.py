from django.contrib import admin
from web.models import Manhwa, Tags, Author, ManhwaList

# Register your models here.


@admin.action(description="Mark manhwas as verified")
def mark_verified(ManhwaAdmin, request, queryset):
    queryset.update(verified=True)


class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Manhwa)
class ManhwaAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "verified", "rating", "image_tag", "created_at")
    actions = [mark_verified]


class TagsAdmin(admin.ModelAdmin):
    pass


class ManhwaListAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(ManhwaList, ManhwaListAdmin)
