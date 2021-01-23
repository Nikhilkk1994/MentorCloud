from django.db import models
from django.utils.translation import ugettext_lazy as _


class PackageSessions(models.Model):
    name = models.CharField(_('Name of Package'), max_length=50)
    description = models.TextField(_('Description of Package'), max_length=5000)
    image = models.ImageField(upload_to='media/package/', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _('Package Session')
        verbose_name_plural = _('Package Sessions')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.name = self.name.lower()
        super(PackageSessions, self).save(force_insert, force_update, using, update_fields)
