from django.contrib import admin
from web.models import Manhwa, Tags, Author

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass


class ManhwaAdmin(admin.ModelAdmin):
    pass


class TagsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Manhwa, ManhwaAdmin)
admin.site.register(Tags, TagsAdmin)
