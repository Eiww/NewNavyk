from django.contrib.auth.mixins import UserPassesTestMixin


class AdminOrManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_superuser or user.groups.filter(name='Manager').exists()
