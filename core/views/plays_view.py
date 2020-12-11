from django.shortcuts import render
from django.views.generic import View
from datetime import date

from core.models import Play


class PlaysView(View):
    def get(self, request):
        plays = Play.objects.all().filter(date__gt=date.today())
        context = {'plays': plays}

        return render(request, 'core/plays.html', context=context)
