from django.urls import path
from .views import *
from app_service import views

app_name = 'app_service'
urlpatterns = [
    path('programs/', ServiceView.as_view(), name='service'),
    path('application/success/<int:pk>/',
         views.application_success_view,
         name='application_success'),
    path('program/<int:pk>/apply/',
         ApplicationCreateView.as_view(),
         name='apply'),
    path('program/<int:pk>/', ProgramDetailView.as_view(), name='program_detail'),
    path('program/<int:pk>/apply/', create_application, name='apply'),
    path('apply/', apply_view, name='apply'),
]
