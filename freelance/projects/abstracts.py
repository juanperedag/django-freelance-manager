from decimal import Decimal
import hashlib
from babeldjango.middleware import get_current_locale
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import to_locale, get_language
from django.utils.translation import ugettext as _

try:
    from pytz import timezone
except ImportError:
    timezone = None

babel = __import__('babel', {}, {}, ['core', 'support'])
Format = babel.support.Format
Locale = babel.core.Locale

__author__ = 'fearless'


def get_upload_path(instance, filename):
    dirname = hashlib.sha256(instance.project.title).hexdigest()[:8]
    return '%s/attachments/%s' % (dirname, filename)


class AbstractAttachment(models.Model):
    """
    Abstract model for Attachment
    """
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=get_upload_path)
    project = models.ForeignKey('freelance.Project', related_name='attachments')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class AbstractType(models.Model):
    """
    Abstract model for Project Type
    """
    title = models.CharField(max_length=255)
    description = models.TextField(help_text=_("Optional description. This field is not private, it will be visible in the printable version of the document."))

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class AbstractTask(models.Model):
    """
    Abstract model for Project Task
    """
    title = models.CharField(max_length=255)
    description = models.TextField(help_text=_("Optional description. This field is not private, it will be visible in the printable version of the document."))
    start_date = models.DateField(null=True, blank=True)
    due_goal = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(User)
    project = models.ForeignKey('freelance.Project')
    visible_to_client = models.BooleanField(default=False)
    progress = models.DecimalField(decimal_places=2, max_digits=4, default='0.00')

    class Meta:
        abstract = True


class AbstractProject(models.Model):
    """
    Abstract model for Project
    """
    title = models.CharField(max_length=255)
    client = models.ForeignKey(User)
    description = models.TextField(help_text=_("Optional description. This field is not private, it will be visible in the printable version of the document."))
    start_date = models.DateField(null=True, blank=True)
    end_goal = models.DateField(null=True, blank=True)
    type = models.ForeignKey('freelance.ProjectType')
    domain = models.CharField(max_length=50, null=True, blank=True)
    sftp_host = models.CharField(max_length=50, null=True, blank=True)
    sftp_password = models.CharField(max_length=50, null=True, blank=True)
    sftp_username = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True

