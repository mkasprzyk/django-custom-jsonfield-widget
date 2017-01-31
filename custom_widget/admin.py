from django.contrib import admin
from custom_widget.models import ReactorModel
from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
import json


class ConditionsWidget(forms.Widget):
    template_name = 'conditions_widget.html'

    def render(self, name, value, attrs=None):
        try:
            conditions = json.loads(value)
        except:
            conditions = []
        context = {
            'id': attrs.get('id'),
            'name': name,
            'condition_choices': ReactorModel.CONDITION_CHOICES,
            'conditions': conditions,
        }
        return mark_safe(render_to_string(self.template_name, context))


class ConditionsForm(forms.ModelForm):
    class Meta:
        model = ReactorModel
        fields = ('name', 'conditions')
        widgets = {
            'conditions': ConditionsWidget,
        }

class ReactorModelAdmin(admin.ModelAdmin):
    form = ConditionsForm


admin.site.register(ReactorModel, ReactorModelAdmin)
