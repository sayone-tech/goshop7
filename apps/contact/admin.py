from django.contrib import admin

from apps.contact.models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact_date',)
    list_filter = ('contact_date',)
    search_fields = ('name', 'email',)

admin.site.register(ContactUs, ContactUsAdmin)
