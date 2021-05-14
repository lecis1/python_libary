from django.urls import path

from . import views


urlpatterns = [
    path('import_data/', views.import_data),
    path('export_data2/', views.export_data),
]