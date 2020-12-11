from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        return render(request, template_name='core/home.html')


class AboutView(View):
    def get(self, request):
        return render(request, template_name='core/about.html')
