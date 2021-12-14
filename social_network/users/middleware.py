from django.utils import timezone
from .models import User


class UpdateLastActivityMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            user = User.objects.get(email__exact=request.user.email)
            user.last_activity = timezone.now()
            user.save()

        return response
