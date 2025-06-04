from django.urls import path
from admin_panel.views import *

app_name = 'admin_panel'
urlpatterns = [
    path('dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('users/', AdminUsersView.as_view(), name='admin_users'),
    path('users/<int:pk>/delete/', AdminUserDeleteView.as_view(), name='admin_user_delete'),
    path('programs/', ProgramListView.as_view(), name='program_list'),
    path('programs/add/', ProgramCreateView.as_view(), name='program_create'),
    path('programs/<int:pk>/edit/', ProgramUpdateView.as_view(), name='program_update'),
    path('programs/<int:pk>/delete/', ProgramDeleteView.as_view(), name='program_delete'),
    path('applications/', ApplicationListView.as_view(), name='application_list'),
    path('applications/<int:pk>/edit/', ApplicationUpdateView.as_view(), name='application_update'),
    path('applications/<int:pk>/delete/', ApplicationDeleteView.as_view(), name='application_delete'),
    path(
        'update-application-status/<int:pk>/',
        update_application_status,
        name='update_application_status'
    ),
    path('faq/list', FAQListView.as_view(), name='faq_list'),
    path('faq/add/', FAQCreateView.as_view(), name='faq_create'),
    path('faq/<int:pk>/edit/', FAQUpdateView.as_view(), name='faq_update'),
    path('faq/<int:pk>/delete/', FAQDeleteView.as_view(), name='faq_delete'),
    path('gallery/add/', GalleryCreateView.as_view(), name='gallery_create'),
    path('gallery/<int:pk>/delete/', GalleryDeleteView.as_view(), name='gallery_delete'),
]
