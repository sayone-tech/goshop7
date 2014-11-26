from django.contrib import admin

from apps.pricing.models import DemoPricing, Features, ActiveDemoPricing


class FeaturesInline(admin.TabularInline):
    model = Features


class DemoPricingAdmin(admin.ModelAdmin):
    inlines = [FeaturesInline, ]
    list_display = ('title', 'price', 'discount_price')
    search_fields = ('title', 'price', 'discount_price' )


class ActiveDemoPricingAdmin(admin.ModelAdmin):
    list_display = ('name', 'demopricing', 'email', 'mobile_no', 'activated_date')
    list_filter = ('demopricing',)
    search_fields = ('name', 'email', 'mobile_no' )

admin.site.register(DemoPricing, DemoPricingAdmin)
admin.site.register(ActiveDemoPricing, ActiveDemoPricingAdmin)
