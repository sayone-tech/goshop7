from django.db import models
from django.utils.translation import ugettext_lazy as _


class SocialLinks(models.Model):
    """
      Model for social links like facebook,google etc...
    """
    CHOICES = (
        ('_blank', 'Blank'),
        ('_top', 'Top'))
    TITLE_FIELDS = (
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('google', 'Google+'))

    title = models.CharField(_("Title"),
            max_length=150, null=True, choices=TITLE_FIELDS)
    link = models.URLField(verbose_name=_('Social Link'),
            max_length=300, null=True,
            help_text="Enter URL For Connecting to Social Media")
    sort_order = models.IntegerField(_("Sort Order"), default=0,)
    targt = models.CharField(_("Target"),
                choices=CHOICES, default='_blank', max_length=20)
    display = models.BooleanField(_("Publish"),
                    default=True, help_text="Check to Publish")

    class Meta:
        verbose_name = _("Social Link")
        verbose_name_plural = _("Social Links")
        ordering = ('sort_order',)

    def __unicode__(self):
        return "%s" % self.title

    @classmethod
    def get_published(self):
        return self.objects.filter(display=True)
