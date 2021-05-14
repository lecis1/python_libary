from django.urls import path

from . import views

urlpatterns = [
    path('export_data/', views.data_export)
]