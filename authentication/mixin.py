from django.contrib.auth.mixins import UserPassesTestMixin

class UserActiveRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_active
            