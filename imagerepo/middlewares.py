from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse
from social_django.middleware import SocialAuthExceptionMiddleware
from social_core.exceptions import AuthAlreadyAssociated, AuthCanceled


class RequestModifierMiddleWares(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.site_name = "Image Repo"
        request.error_message = request.session.pop("error_message", "")
        return self.get_response(request)


class AuthAlreadyAssociatedMiddleware(SocialAuthExceptionMiddleware):
    """Redirect users to desired-url when AuthAlreadyAssociated exception occurs."""

    def process_exception(self, request, exception):
        if isinstance(exception, AuthAlreadyAssociated) or isinstance(exception, AuthCanceled):
            logout(request)
            return redirect(reverse("accounts:login"))
