from django.urls import path
from .views import image_processing, form_view


app_name = 'core'

urlpatterns = [
    path('core_api/', image_processing, name="core_api"),
    path('image/', form_view, name='form_view')
]