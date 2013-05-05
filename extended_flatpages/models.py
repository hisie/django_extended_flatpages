from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

class CMSFlatPage(FlatPage):
    description = models.CharField(verbose_name=_(u"Description"),max_length=100)
    keywords = models.CharField(verbose_name=_(u"Keywords"),max_length=255)