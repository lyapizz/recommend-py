from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', login_required(views.IndexView.as_view()), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('home/', views.home, name='home'),
    path('top/', views.top, name='top'),
    path('profile/', views.profile, name='profile'),
]