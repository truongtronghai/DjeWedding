from django.contrib import admin
from .models import Block


class BlockAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'description',
        'short_text_1',
        'short_text_2',
        'short_text_3',
        'short_text_4',
        'getImageTag',
        'enabled'
    )


# Register your models here.
admin.site.register(Block, BlockAdmin)
