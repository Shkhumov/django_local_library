from django.forms import ModelForm

from .models import  Callback


class CallbackForm(ModelForm):
    class Meta:
        model = Callback
        fields = [
            'call_name',
            'call_phone',
        ]