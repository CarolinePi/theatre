from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from core.models import Worker


class ActorView(View):

    def get(self, request, pk):
        actor = get_object_or_404(Worker, pk=pk)
        if actor.position.title != "Actor":
            # TODO: make a 404 page and render it!!!
            return render(request, 'core/home.html', status=404)

        roles = actor.role_set.all()

        context = {"actor": actor, "roles": roles}
        return render(request, "core/actor.html", context=context)



