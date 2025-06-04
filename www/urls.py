from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('privacy-policy/', PrivacyPolicyPageView.as_view(), name='privacy-policy'),
    path('agreement/', AgreementPageView.as_view(), name='agreement'),
    path('rekvizity/', RekvizityPageView.as_view(), name='rekvizity'),
    path('schedule/', SchedulePageView.as_view(), name='schedule'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
    path('faq/', faq_view, name='faq'),

]
