from django.db import models
from django.template.loader import select_template
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

class GoogleFormsPlugin(CMSPlugin):
    form_id = models.CharField(_('form key'),max_length=64)
    height = models.PositiveIntegerField(null=True, blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)
    
    @property
    def render_template(self):
        return select_template([
        'cms/plugins/googleform/%s-form.html' % (self.placeholder.slot.lower(),),
        'cms/plugins/googleform/form.html'])
