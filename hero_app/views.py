from django.http import JsonResponse
from django.views import View
from .models import Hero
import json

class Heros(View):
    def get(self, request):
        heroes = list(Hero.objects.values().all())
        return JsonResponse({'status': 'ok', "heroes": heroes})

    def post(self, request):
        body = json.loads(request.body.decode())
        print(body)
        # Hero.objects.create(
        #     alias = body['alias'],
        #     secret = body['secret'],
        #     description = body['description']
        # )
        Hero.objects.create_hero(body)
        return JsonResponse({'status': 'ok', "message": "it was a post this time"})
