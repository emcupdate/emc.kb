from plone.app.registry.browser import controlpanel

from emc.kb.interfaces import ILogSettings
from emc.kb import _

try:
    # only in z3c.form 2.0
    from z3c.form.browser.textlines import TextLinesFieldWidget
except ImportError:
    from plone.z3cform.textlines import TextLinesFieldWidget

class LogSettingsEditForm(controlpanel.RegistryEditForm):
    
    schema = ILogSettings
    label = _(u"Log settings") 
    description = _(u"Please enter details of log")
    
    def updateFields(self):
        super(LogSettingsEditForm, self).updateFields()
        self.fields['timeout'].widgetFactory = TextLinesFieldWidget
        self.fields['max'].widgetFactory = TextLinesFieldWidget
        self.fields['percentage'].widgetFactory = TextLinesFieldWidget        
        self.fields['bsize'].widgetFactory = TextLinesFieldWidget

    
class LogSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = LogSettingsEditForm