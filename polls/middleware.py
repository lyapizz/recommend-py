import time

from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin
from social_core.exceptions import AuthCanceled
from social_django.middleware import SocialAuthExceptionMiddleware


class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if exception.__class__ == AuthCanceled:
            print('AuthCanceledException: ', exception)
            return render(request, template_name='polls/home.html')
        else:
            raise exception


class StatsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        "Start time at request coming in"
        request.start_time = time.time()

    def process_response(self, request, response):
        "End of request, take time"
        total = time.time() - request.start_time

        # Add the header.
        response["X-total-time"] = int(total * 1000)
        return response
