from django.forms import ModelForm
from .models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = [
            'text',
        ]
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['text'].widget.attrs.update({'class': 'textarea', 'placeholder': 'what\'s on your mind right now?'})