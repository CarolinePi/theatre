from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from core.models import Worker, Author


class DirectorView(View):

    def get(self, request, pk):
        director = get_object_or_404(Worker, pk=pk)
        if director.position.title != "Director":
            # TODO: make a 404 page and render it!!!
            return render(request, 'core/home.html', status=404)

        performances = director.performance_set.all()

        context = {"director": director, "performances": performances}
        return render(request, "core/director.html", context=context)

