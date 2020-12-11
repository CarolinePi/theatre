from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from core.models import Play


#TODO: BUY TICKET HERE
class PlayView(View):

    def get(self, request, pk):
        play = get_object_or_404(Play, pk=pk)

        context = {'play': play}
        return render(request, template_name='core/play.html', context=context)
