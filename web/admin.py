from django.contrib import admin
from django.contrib import messages
from web.models import Manhwa, Tags, Author, ManhwaList

# Register your models here.


@admin.action(description="Mark manhwas as verified")
def mark_verified(ManhwaAdmin, request, queryset):
    if (
        queryset.filter(verification_status=Manhwa.VERIFICATION_STATUS_REJECTED).count()
        > 0
    ):
        messages.error(request, "Rejected Manhwas cannot be marked as verified")
    else:
        queryset.update(verified=True)
        queryset.update(verification_status=Manhwa.VERIFICATION_STATUS_VERIFIED)
        messages.success(request, "Manhwas marked as verified")


@admin.action(description="Mark manhwas as rejected")
def mark_rejected(ManhwaAdmin, request, queryset):
    if (
        queryset.filter(verification_status=Manhwa.VERIFICATION_STATUS_VERIFIED).count()
        > 0
    ):
        messages.error(request, "Verified Manhwas cannot be marked as rejected")
    else:
        queryset.update(verified=False)
        queryset.update(verification_status=Manhwa.VERIFICATION_STATUS_REJECTED)
        messages.success(request, "Manhwas marked as rejected")


class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Manhwa)
class ManhwaAdmin(admin.ModelAdmin):
    list_display = ("title", "verification_icon", "image_tag", "description")
    actions = [mark_verified, mark_rejected]
    search_fields = ["title", "description"]

    def verification_icon(self, obj):
        if obj.verification_status == obj.VERIFICATION_STATUS_VERIFIED:
            return True
        elif obj.verification_status == obj.VERIFICATION_STATUS_REJECTED:
            return False
        else:
            return None

    verification_icon.boolean = True


class TagsAdmin(admin.ModelAdmin):
    pass


class ManhwaListAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(ManhwaList, ManhwaListAdmin)
