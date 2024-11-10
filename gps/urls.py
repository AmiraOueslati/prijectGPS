from django.urls import path
from .views import GPSDataView  # Vérifiez que la vue est bien importée

urlpatterns = [
    path('receive_gps_data/', GPSDataView, name='receive_gps_data'),
]
