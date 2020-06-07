"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from registration.backends.simple.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

from mysite.settings import LOGIN_REDIRECT_URL

urlpatterns = [
    path('', RedirectView.as_view(url='/polls/1/#hello')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace="social")),
    url(r'^ratings/', include('polls.urls_stars', namespace='ratings')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/polls/images/favicon.ico')),
    url(r'^accounts/register/$',
        RegistrationView.as_view(form_class=RegistrationFormUniqueEmail,
                                 template_name='registration/registration_form.html',
                                 success_url=LOGIN_REDIRECT_URL),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
