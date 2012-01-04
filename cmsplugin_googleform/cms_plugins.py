from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_googleform.models import GoogleFormsPlugin


class CMSGoogleFormsPlugin(CMSPluginBase):
    model = UpcomingEventsPlugin
    name = _('Google Forms Plugin')
    render_template = 'cms/plugins/googleform/form.html'
    
    def render(self, context, instance, placeholder):
        form = '<iframe src="https://docs.google.com/spreadsheet/embeddedform?formkey=dDk3TE1nejVOV0tkLUJtbXYzV0pDVnc6MQ" width="760" height="639" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>'
        context.update({'form': form })
        
        return context

plugin_pool.register_plugin(CMSGoogleFormsPlugin)

