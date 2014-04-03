from django.db import models
from django.utils.translation import ugettext_lazy as _

class BaseEntity(models.Model):
    active = models.BooleanField(_('Active'), default = True)
    name = models.CharField(_('Entity'), max_length = 255, db_index = True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

class University(BaseEntity):

    class Meta:
        verbose_name_plural = 'Universities'

class Course(BaseEntity):
    code = models.CharField(max_length = 10)
    university = models.ForeignKey(University)

    class Meta:
        verbose_name_plural = 'Courses'
