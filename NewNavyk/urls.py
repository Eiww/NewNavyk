from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from www.views import logout_page

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('www.urls')),
                  path('service/', include('app_service.urls')),
                  path('admin_panel/', include('admin_panel.urls')),
                  path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
                  path('logout/', logout_page, name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
