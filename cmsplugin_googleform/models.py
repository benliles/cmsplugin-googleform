from django.db import models
from django.template.loader import select_template
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

class GoogleFormsPlugin(CMSPlugin):
    form_id = models.CharField(max_length=64)
    template = models.CharField(max_length=255, null=True, blank=True)
    
    @property
    def render_template(self):
        if self.template:
            return self.template
        
        return select_template([
            'cms/plugins/googleform/%s-form.html' % (self.placeholder.slot.lower(),),
            'cms/plugins/googleform/form.html'])
