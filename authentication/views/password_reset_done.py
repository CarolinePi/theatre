from django.shortcuts import render
from django.views import View


class PasswordResetDone(View):
    template_name = 'registration/password_reset_done.html'

    def get(self, request):
        return render(request, self.template_name)
