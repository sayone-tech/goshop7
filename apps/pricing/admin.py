from django.contrib import admin

from apps.pricing.models import DemoPricing, Features, ActiveDemoPricing


class FeaturesInline(admin.TabularInline):
    model = Features


class DemoPricingAdmin(admin.ModelAdmin):
    inlines = [FeaturesInline, ]


class ActiveDemoPricingAdmin(admin.ModelAdmin):
    pass

admin.site.register(DemoPricing, DemoPricingAdmin)
admin.site.register(ActiveDemoPricing, ActiveDemoPricingAdmin)
