from .models import Snake
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class SnakeForm(ModelForm):
    class Meta:
        model = Snake
        fields = ['title', 'anons', 'text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
        }