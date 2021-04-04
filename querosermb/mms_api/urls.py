from django.urls import include, path, re_path
from .views import CriptoValoresViewSet
app_name = 'mms_api'
urlpatterns = [
    re_path('^(?P<pair>.+)/(?P<mms>.+)/$', CriptoValoresViewSet.as_view(), name="criptovalores")
]