from django.conf.urls import url

from star_ratings import app_settings
from .views import Rate

app_name = 'polls'

urlpatterns = [
    url(r'(?P<content_type_id>\d+)/(?P<object_id>' + app_settings.STAR_RATINGS_OBJECT_ID_PATTERN + ')/', Rate.as_view(),
        name='rate'),

]
