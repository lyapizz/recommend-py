from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', login_required(views.IndexView.as_view()), name='index'),
    # ex: /polls/5/
    path('<int:id>/', views.detail, name='detail'),
    # ex: /polls/5/next
    path('<int:id>/<str:action>', views.detail, name='detail'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('top/', views.top, name='top'),
    path('profile/', views.profile, name='profile'),
]
