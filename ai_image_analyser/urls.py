from django.urls import path
from .views import image_analysis_view

urlpatterns = [
    path('', image_analysis_view, name='image_analysis_view'),
]