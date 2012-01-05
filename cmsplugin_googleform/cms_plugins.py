from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_googleform.models import GoogleFormsPlugin


class CMSGoogleFormsPlugin(CMSPluginBase):
    model = GoogleFormsPlugin
    name = _('Google Forms Plugin')
    render_template = 'cms/plugins/googleform/form.html'
    
    def render(self, context, instance, placeholder):
        form_key = instance.form_id
        context.update({'form': form_key })
        
        return context

plugin_pool.register_plugin(CMSGoogleFormsPlugin)

