from django.contrib.auth.models import User

class EmailAuthBackend(object):
    """Authenticate using an e-mail address."""

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    # We get a user through the ID set in the user_id parameter.
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
