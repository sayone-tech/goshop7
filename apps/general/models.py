from django.db import models
from django.contrib.sites.models import Site


class GeneralSettings(models.Model):
    site = models.OneToOneField(Site, related_name='site_settings')
    start = models.PositiveSmallIntegerField(default=0)
    end  = models.PositiveSmallIntegerField(default=30)
    now = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return self.site.name
    

