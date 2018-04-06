from django.contrib import admin
from . import models


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'created_at',
        'updated_at',
        'file',
        'location',
        'caption',
        'creator',
        # 'tags',
    )
    search_fields = ('location', 'caption', 'creator__username',)
    # autocomplete_fields = ('location',)


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'created_at',
        'updated_at',
        'creator',
        'image',
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'created_at',
        'updated_at',
        'message',
        'creator',
        'image',
    )


