from django import forms
from .models import Services, Request
from bootstrap_datepicker_plus import DatePickerInput

class ServiceForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Services.objects.all(), initial=0, label="Послуги")
    date_begin = forms.DateField(widget=DatePickerInput(format='%d.%m.%Y'), label="Дата початку роботи")

    class Meta:
        model = Request
        fields = ['car', 'service', 'add_info', 'date_begin', 'urgently']