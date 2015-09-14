from django.contrib import admin
from fetr.models import Album, Image

class AlbumInLine(admin.StackedInline):
    model = Image
    extra = 1


class FetrAdmin(admin.ModelAdmin):
    inlines = [
        AlbumInLine,

               ]
# Register your models here.

admin.site.register(Album, FetrAdmin)
