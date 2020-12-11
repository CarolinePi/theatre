from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from core.models import Author


class AuthorsView(View):
    def get(self, request):
        authors = Author.objects.all()

        context = {"authors": authors}
        return render(request, "core/authors.html", context=context)
