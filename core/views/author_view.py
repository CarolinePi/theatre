from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from core.models import Author


class AuthorView(View):

    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        performances = author.performance_set.all()

        context = {"author": author, "performances": performances}
        return render(request, "core/author.html", context=context)



