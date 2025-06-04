from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test


def admin_or_manager_required(view_func):
    def check_user(user):
        return user.is_superuser or user.groups.filter(name='Manager').exists()

    decorated_view = user_passes_test(check_user, login_url='/')
    return decorated_view(view_func)
