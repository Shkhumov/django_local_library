# -*- coding: utf-8 -*-

from .models import Price
from django.forms import ModelForm

class PriceForm(ModelForm):
    class Meta:
        model = Price
        fields = ['threshold']


