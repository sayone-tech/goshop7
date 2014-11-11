from django.contrib import admin
from models import SocialLinks


class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ['title', 'sort_order', 'display', ]
    list_editable = ['sort_order', 'display', ]
    search_fields = ('title', 'link', 'targt')
    list_filter = ('targt', )

admin.site.register(SocialLinks, SocialLinksAdmin)
