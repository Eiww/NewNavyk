from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from app_service.forms import PublicApplicationForm
from app_service.models import *


class ServiceView(ListView):
    model = Program
    template_name = 'app_service/service.html'
    context_object_name = 'programs'


def application_success_view(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'app_service/application_success.html', {
        'program_price': program.price,
    })


class ApplicationCreateView(CreateView):
    model = Application
    form_class = PublicApplicationForm
    template_name = 'app_service/application_form.html'

    def form_valid(self, form):
        program = get_object_or_404(Program, pk=self.kwargs['pk'])
        form.instance.program = program
        response = super().form_valid(form)

        send_mail(
            'Новая заявка',
            'Поступила новая заявка на обучение.',
            'niktonikakoj0@gmail.com',
            ['niktonikakoj0@gmail.com'],
            fail_silently=False,
        )

        return response

    def get_success_url(self):
        return reverse('app_service:application_success', kwargs={'pk': self.kwargs['pk']})


class ProgramDetailView(DetailView):
    model = Program
    template_name = 'app_service/program_detail.html'
    context_object_name = 'program'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PublicApplicationForm()
        return context


def create_application(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        form = PublicApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.program = program
            application.save()
            return redirect('application_success')
    return redirect('program_detail', pk=pk)


def apply_view(request):
    if request.method == 'POST':
        program = get_object_or_404(Program, id=request.POST.get('program_id'))
        Application.objects.create(
            program=program,
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email')
        )
        return redirect('app_service:application_success', pk=program.pk)
    return redirect('app_service:service')
