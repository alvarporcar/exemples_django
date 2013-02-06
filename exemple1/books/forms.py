from django import forms
from models import Publisher
from django.forms import ModelForm

TOPIC_CHOICES = (
            ('general', 'Peticio General'),
            ('bug', 'Informe Error'),
            ('suggestion','Sugerencia'),
        )

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices = TOPIC_CHOICES)
    messages = forms.CharField(widget = forms.Textarea())
    sender = forms.EmailField(required = False)

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher

