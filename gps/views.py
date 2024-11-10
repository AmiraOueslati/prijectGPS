from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from mongoengine import Document, FloatField
from mongoengine import connect

# Connecter MongoDB
connect('GPS_DATA', host='mongodb://localhost:27017/GPS_DATA')

# Définir le modèle MongoDB
class GPSData(Document):
    latitude = FloatField()
    longitude = FloatField()

@csrf_exempt
def GPSDataView(request):
    print(f"Method: {request.method}") 
    if request.method == 'POST':
        try:
            # Récupérer les données JSON envoyées
            data = json.loads(request.body)
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            
            if latitude is None or longitude is None:
                return JsonResponse({'message': 'Latitude ou Longitude manquants'}, status=400)
            
            # Sauvegarder les données dans MongoDB
            data_gps = GPSData(latitude=latitude, longitude=longitude)
            data_gps.save()

            # Retourner une réponse avec les données et un message de confirmation
            return JsonResponse({
                'message': 'Données GPS reçues et enregistrées',
                'latitude': latitude,
                'longitude': longitude
            })

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Erreur de décodage JSON'}, status=400)
    return JsonResponse({'message': 'Méthode non autorisée'}, status=405)
