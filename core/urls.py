from django.urls import path
from .views import image_processing


app_name = 'core'

urlpatterns = [
    path('core_api/', image_processing, name="core_api"),
]