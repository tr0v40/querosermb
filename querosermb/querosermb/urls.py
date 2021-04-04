from django.urls import include, path

urlpatterns = [
    path('', include('mms_api.urls', namespace="mms_api"))
]