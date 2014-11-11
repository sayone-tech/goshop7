from apps.newsletter.models import *
from django.contrib import admin

class NewsletterAdmin(admin.ModelAdmin):
    list_display=('email','confirm',)
    search_fields = ['email']

admin.site.register(NewsletterSubscription,NewsletterAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display=('title','send','is_sent',)
    list_editable=('send',)

admin.site.register(Newsletter,NewsAdmin)
