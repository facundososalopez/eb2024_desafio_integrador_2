from django.contrib.auth.mixins import UserPassesTestMixin

class TestStaffMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser