from django.contrib import admin
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cmsplugin_tabs.models import TabHeader, Tab


class TabHeaderPlugin(CMSPluginBase):
    model = TabHeader
    name = "Tabs Header"
    render_template = "cmsplugin_tabs/tabheader.html"
    allow_children = True
    child_classes = ["TabPlugin"]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            })
        return context


class TabPlugin(CMSPluginBase):
    model = Tab
    name = "Tab"
    render_template = "cmsplugin_tabs/tab.html"
    parent_classes = ["TabHeaderPlugin"]
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            })
        return context

plugin_pool.register_plugin(TabPlugin)
plugin_pool.register_plugin(TabHeaderPlugin)
