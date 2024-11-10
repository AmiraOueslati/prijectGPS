from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass  # Tu peux ajouter des champs comme prénom, téléphone, etc.
