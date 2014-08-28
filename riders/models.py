from django.db import models
from markupfield.fields import MarkupField
from django.contrib.auth.models import User


def content_file_name(instance, filename):
        return '/'.join(['content', instance.user.username, filename])


class RiderProfile(models.Model):
    # Link to main user record
    user = models.OneToOneField(User, primary_key = True)

    # Extended User Information
    company = models.CharField(max_length=200, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)

    biography = MarkupField(null=True, blank=True, markup_type='markdown')
    statement = MarkupField(null=True, blank=True, markup_type='markdown')

    avatar = models.ImageField(upload_to=content_file_name)
    banner = models.ImageField(upload_to=content_file_name)

    def __unicode__(self):
        return self.user.username

    class Meta:
        db_table    = "riders_profiles"
        app_label   = 'riders'