from django.db import models
from django.utils.translation import ugettext_lazy as _


class Testimonial(models.Model):
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    company_name = models.CharField(_('Company Name'), max_length=50)
    description = models.TextField(_('description'), max_length=5000)
    image = models.ImageField(upload_to='media/testimonial/', max_length=255)

    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.company_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.first_name = self.first_name.lower()
        self.last_name = self.last_name.lower()
        self.company_name = self.company_name.lower()
        super(Testimonial, self).save(force_insert, force_update, using, update_fields)
