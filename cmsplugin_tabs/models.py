from django.db import models
from cms.models import CMSPlugin


class TabHeader(CMSPlugin):
    """
    A plugin that has Tab classes as children.
    """
    def __unicode__(self):
        return u"{0} tabs".format(self.cmsplugin_set.all().count())


class Tab(CMSPlugin):
    """
    An individual Tab for the TabHeader plugin.
    """
    title = models.CharField(max_length=64)

    def __unicode__(self):
        return u"{0}".format(self.title)
