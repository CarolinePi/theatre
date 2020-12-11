from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from authentication.forms import LoginForm


class LoginView(View):
    form = LoginForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:home')

        context = {'form': self.form, 'message': ''}
        return render(request, 'registration/login.html', context=context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            user_info = form.cleaned_data
            user = authenticate(username=user_info['username'], password=user_info['password'])
        else:
            return HttpResponse(status=404)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('core:home')
            else:
                message = "Login is not active"
        else:
            message = "Wrong login or password"

        context = {'form': self.form, 'message': message}
        return render(request, 'registration/login.html', context=context)
