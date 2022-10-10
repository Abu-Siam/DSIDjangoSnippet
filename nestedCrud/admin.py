from django.contrib import admin

from nestedCrud.models import Singer, Song


# Register your models here.
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'singer', 'duration')