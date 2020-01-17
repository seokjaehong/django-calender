from django.forms import ModelForm, DateInput, ChoiceField
from .models import Event


class EventForm(ModelForm):
    repeat = ChoiceField(choices=([('N', "NONE"), ('W', 'WEEKLY'), ('M', 'MONTHLY')]), initial='N', required=True)

    class Meta:
        model = Event
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = ('title', 'description', 'budget', 'start_time', 'end_time', 'repeat')

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
