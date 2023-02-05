from django import forms

from .models import Report


class ReportForm(forms.ModelForm):
    date_of_accident = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time_of_accident = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Report
        fields = ['witness_name', 'witness_email', 'witness_phonenumber', 'date_of_accident', 'time_of_accident', 'accident_type', 'is_fatal', 'image', 'video', 'witness_involvement', 'number_of_vehicles_involved', 'number_of_injured_victims', 'cause_of_accident', 'number_of_deaths', 'location', 'type_of_road', 'description']

