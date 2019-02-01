
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from mymusic.models import User

LOGIN_REQUIRED = []

class LoginMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if request.path in LOGIN_REQUIRED:
            user_id = request.session.get("user_id")
            if user_id:
                user = User.objects.get(pk=user_id)
                request.user = user
            else:
                return redirect(reverse('login'))
