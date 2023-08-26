from django import forms
from django.core.exceptions import ValidationError

from .models import Advertisement

class AdvertisementForms(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ["title", "descriptional", "image", "price", "auction"]
        widget = {
            'title' : forms.TextInput(attrs={'class' : 'form-control form-control-lg'}),
            'descriptional' : forms.Textarea(attrs={'class' : 'form-control form-control-lg'}),
            'price' : forms.NumberInput(attrs={'class' : 'form-control form-control-lg'}),
            'auction' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
            'image' : forms.FileInput(attrs={'class' : 'form-control form-control-lg'}),
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с вопросительного знака.')
        return title
