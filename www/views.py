from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from app_service.models import FAQ, Gallery, Program


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'gallery_photos': Gallery.objects.all(),
        })
        return context


class PrivacyPolicyPageView(TemplateView):
    template_name = 'www/privacy-policy.html'


class AgreementPageView(TemplateView):
    template_name = 'www/agreement.html'


class RekvizityPageView(TemplateView):
    template_name = 'www/rekvizity.html'


class ContactPageView(TemplateView):
    template_name = 'www/contacts.html'


class SchedulePageView(TemplateView):
    template_name = 'www/schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'programs': Program.objects.all(),
        })
        return context


def faq_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'www/faq.html', {'faq_list': faqs})


def logout_page(request):
    logout(request)
    return redirect('home')
