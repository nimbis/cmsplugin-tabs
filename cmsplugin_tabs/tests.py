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
        self.assertEquals(self.header.__unicode__(), "0 tabs")
        self.assertEquals(self.tab.__unicode__(), "Test Tab")