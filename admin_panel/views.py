from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, DeleteView, UpdateView, CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from app_service.models import *
from .forms import ProgramForm, ApplicationForm
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


def is_in_group(user, group_name):
    try:
        return user.groups.filter(name=group_name).exists()
    except Exception:
        return False


class AdminOrManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or is_in_group(self.request.user, 'manager')


@login_required
@require_http_methods(["POST"])
def update_application_status(request, pk):
    try:
        application = Application.objects.get(pk=pk)
        new_status = json.loads(request.body).get('status')

        if new_status in dict(Application.STATUS_CHOICES).keys():
            application.status = new_status
            application.save()
            return JsonResponse({
                'status': 'success',
                'status_display': application.get_status_display()
            })

        return JsonResponse(
            {'status': 'error', 'error': 'Invalid status'},
            status=400
        )

    except Application.DoesNotExist:
        return JsonResponse(
            {'status': 'error', 'error': 'Application not found'},
            status=404
        )

    except Exception as e:
        return JsonResponse(
            {'status': 'error', 'error': str(e)},
            status=500
        )


class AdminDashboardView(LoginRequiredMixin, AdminOrManagerRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'admin_panel/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'gallery_photos': Gallery.objects.all()[:8],
            'programs_count': Program.objects.count(),
            'faq_count': FAQ.objects.count(),
            'users_count': User.objects.count(),
            'applications': Application.objects.all().order_by('-created_at')[:5],
            'all_applications': Application.objects.all().order_by('-created_at')
        })
        return context


class AdminUsersView(LoginRequiredMixin, AdminOrManagerRequiredMixin, ListView):
    model = User
    template_name = 'admin_panel/users.html'
    context_object_name = 'users'


class AdminUserDeleteView(LoginRequiredMixin, AdminOrManagerRequiredMixin, DeleteView):
    model = User
    template_name = 'admin_panel/user_delete.html'
    success_url = reverse_lazy('admin_panel:admin_users')


class ProgramCreateView(LoginRequiredMixin, AdminOrManagerRequiredMixin, CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'admin_panel/programs/form.html'
    success_url = reverse_lazy('admin_panel:program_list')


class ProgramUpdateView(LoginRequiredMixin, AdminOrManagerRequiredMixin, UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'admin_panel/programs/form.html'
    success_url = reverse_lazy('admin_panel:program_list')


class ProgramDeleteView(LoginRequiredMixin, AdminOrManagerRequiredMixin, DeleteView):
    model = Program
    template_name = 'admin_panel/programs/confirm_delete.html'
    success_url = reverse_lazy('admin_panel:program_list')


class ProgramListView(LoginRequiredMixin, AdminOrManagerRequiredMixin, ListView):
    model = Program
    template_name = 'admin_panel/programs/list.html'
    context_object_name = 'programs'
    paginate_by = 10
    ordering = ['id']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Program.objects.filter(title__icontains=query)
        return super().get_queryset()


class ApplicationListView(LoginRequiredMixin, AdminOrManagerRequiredMixin, ListView):
    model = Application
    template_name = 'admin_panel/applications/list.html'
    context_object_name = 'applications'
    paginate_by = 20
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        if status:
            return queryset.filter(status=status)
        return queryset


class ApplicationUpdateView(LoginRequiredMixin, AdminOrManagerRequiredMixin, UpdateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'admin_panel/applications/form.html'
    success_url = reverse_lazy('admin_panel:application_list')


class ApplicationDeleteView(LoginRequiredMixin, AdminOrManagerRequiredMixin, DeleteView):
    model = Application
    template_name = 'admin_panel/applications/confirm_delete.html'
    success_url = reverse_lazy('admin_panel:application_list')


class FAQListView(ListView):
    model = FAQ
    template_name = 'admin_panel/faq/faq_list.html'
    context_object_name = 'faqs'
    paginate_by = 10


class FAQCreateView(CreateView):
    model = FAQ
    fields = ['question', 'answer']
    template_name = 'admin_panel/faq/form.html'
    success_url = reverse_lazy('admin_panel:faq_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить новый вопрос'
        return context


class FAQUpdateView(UpdateView):
    model = FAQ
    fields = ['question', 'answer']
    template_name = 'admin_panel/faq/form.html'
    success_url = reverse_lazy('admin_panel:faq_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать вопрос'
        return context


class FAQDeleteView(DeleteView):
    model = FAQ
    template_name = 'admin_panel/faq/delete.html'
    success_url = reverse_lazy('admin_panel:faq_list')


class GalleryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Gallery
    fields = ['image']
    template_name = 'admin_panel/gallery_form.html'
    success_url = reverse_lazy('admin_panel:admin_dashboard')

    def test_func(self):
        return self.request.user.is_superuser


class GalleryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Gallery
    success_url = reverse_lazy('admin_panel:admin_dashboard')

    def test_func(self):
        return self.request.user.is_superuser
