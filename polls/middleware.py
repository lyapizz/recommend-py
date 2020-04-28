from django.shortcuts import render
from social_core.exceptions import AuthCanceled
from social_django.middleware import SocialAuthExceptionMiddleware


class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if exception.__class__ == AuthCanceled:
            print('AuthCanceledException: ', exception)
            return render(request, template_name='polls/home.html')
        else:
            raise exception
