from django import forms
from django.contrib import admin
from app_service.models import *


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question', 'answer')
    list_editable = ('answer',)
    save_on_top = True


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
        widgets = {
            'benefits_list': forms.Textarea(attrs={'rows': 5}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }
