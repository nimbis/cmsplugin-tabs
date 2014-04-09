from django.test import TestCase
from models import Tab, TabHeader


class TabsTest(TestCase):
    """
    Simple CRUD test for cmsplugin-tabs
    """

    def setUp(self):
        self.tab = Tab()
        self.tab.title = "Test Tab"
        self.header = TabHeader()

    def test_plugin(self):
        self.assertEquals(unicode(self.header), "0 tabs")
        self.assertEquals(unicode(self.tab), "Test Tab")