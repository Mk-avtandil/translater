from .models import WordFromUser, Word
from django.forms import ModelForm, TextInput

class InputForm(ModelForm):
    class Meta: 
        model = WordFromUser
        fields = ['user_word']
        widgets = {
            'user_word': TextInput(attrs={
            'type': 'text',
            'placeholder': 'Введите слово',
            'autocomplete': 'off'})}

class SendWords(ModelForm):
    class Meta: 
        model = Word
        fields = ['en', 'ru']
        widgets = {
            'en': TextInput(attrs={
            'type': 'text',
            'placeholder': 'Английский',
            'autocomplete': 'off'
            }),
            
            'ru': TextInput(attrs={
            'type': 'text',
            'placeholder': 'Русский',
            'autocomplete': 'off'
            }),
            }