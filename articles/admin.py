from django.contrib import admin

from .models import Article, Visitor, Bridge

class BridgAdmin(admin.ModelAdmin):
    list_display = ('stars', 'visitor', 'article')

admin.site.register(Article)
admin.site.register(Visitor)
admin.site.register(Bridge, BridgAdmin)
