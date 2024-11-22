from django.contrib.auth.backends import BaseBackend

from apps.common.services.pgadmin.models import UserAccount


class UserAccountBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = UserAccount.objects.get(username=username)
            if user.check_password(password):
                return user
        except UserAccount.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserAccount.objects.get(pk=user_id)
        except UserAccount.DoesNotExist:
            return None
