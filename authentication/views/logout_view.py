from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import View


class LogoutView(LoginRequiredMixin, View):
    def post(self, request):
        logout(request)
        return redirect('core:home')
