from django.contrib import admin

from .models import Article, Visitor, Bridge

class BridgAdmin(admin.ModelAdmin):
    list_display = ('stars', 'visitor', 'article')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rate')
    list_filter = ('rate',)
    ordering = ('rate',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Visitor)
admin.site.register(Bridge, BridgAdmin)
