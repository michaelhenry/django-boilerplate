from django.db import models
from django.conf import settings
from django.dispatch import receiver


class HasTimeStamped(models.Model):

  created   =  models.DateTimeField(auto_now_add=True)
  modified  =  models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class HasUserInfo(models.Model):

  created_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    related_name='%(class)s_creators',
    on_delete=models.CASCADE,
    null=True,
    blank=True,
  )

  modified_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    related_name='%(class)s_modifiers',
    on_delete=models.CASCADE,
    null=True,
    blank=True,
  )

  class Meta(object):
    abstract = True
