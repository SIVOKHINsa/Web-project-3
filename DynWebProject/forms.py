from .models import articles
from django.forms import ModelForm, TextInput, DateInput, Textarea

class articlesform(ModelForm):
    class Meta:
        model = articles
        fields = ['title', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'formcontrol',
                'placeholder': 'Название статьи'
            }),
            "date": DateInput(attrs={
                'class': 'formcontrol',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'formcontrol',
                'placeholder': 'Текс статьи'
            })
        }

