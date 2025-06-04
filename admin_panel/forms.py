from django import forms
from django.core.exceptions import ValidationError
from app_service.models import *


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
        widgets = {
            'category': forms.CheckboxSelectMultiple(
                attrs={'class': 'category-checkboxes'}
            ),
            'benefits_list': forms.Textarea(attrs={'rows': 4}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'start_date': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local'
                }
            ),
        }
        help_texts = {
            'category': 'Выберите одну или несколько категорий',
            'benefits_list': 'Перечислите каждый плюс программы с новой строки',
            'start_date': 'Назначьте дату и время проведения мероприятия',
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if self.instance and self.instance.start_date:
                self.initial['start_date'] = self.instance.start_date.strftime('%Y-%m-%dT%H:%M')

        def clean_image(self):
            image = self.cleaned_data.get('image')
            if image:
                if image.size > 5 * 1024 * 1024:  # 5MB
                    raise ValidationError("Максимальный размер файла 5MB")
                if not image.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                    raise ValidationError("Допустимые форматы: JPG, JPEG, PNG")
            return image


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['status', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'})
        }
