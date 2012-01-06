from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_googleform.models import GoogleFormsPlugin


class CMSGoogleFormsPlugin(CMSPluginBase):
    model = GoogleFormsPlugin
    name = _('Google Forms Plugin')
    render_template = 'cms/plugins/googleform/form.html'
    
    def render(self, context, instance, placeholder):
        context.update({'form_key': instance.form_id,
                        'form_width': instance.width,
                        'form_height': instance.height
                         })
        return context

plugin_pool.register_plugin(CMSGoogleFormsPlugin)

