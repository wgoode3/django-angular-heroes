from django.db import models
from django.conf import settings
import os, base64 

ALLOWED_EXTENSIONS = ("jpg", "jpeg", "png", "gif") 

class HeroManager(models.Manager):

    def create_hero(self, data):
        hero = Hero(
            alias=data["alias"],
            secret=data["secret"],
            description=data["description"]
        )
        extension = data['filename'].split('.')[-1].lower()
        if extension in ALLOWED_EXTENSIONS:
            img_path = os.path.join(settings.MEDIA_ROOT, data["filename"])
            with open(img_path, 'wb') as img:
                img.write(base64.b64decode(data['image'].split(',')[-1]))
                hero.image = data['filename']
        else:
            hero.image = "default.jpg"
        hero.save()

class Hero(models.Model):
    alias = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    objects = HeroManager()