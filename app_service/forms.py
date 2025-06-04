from django import forms
from .models import Application


class PublicApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'phone', 'email', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Ваши дополнительные пожелания или вопросы'
            })
        }
