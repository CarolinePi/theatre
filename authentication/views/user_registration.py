from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View

from authentication.forms import CustomerRegistrationForm


class UserRegistration(View):
    form = CustomerRegistrationForm
    template_name = 'registration/signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:home')

        context = {'form': self.form, 'message': ''}
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                User.objects.get(email=email)
                context = {'form': self.form, 'message': "User with this email is already exists"}
                return render(request, self.template_name, context=context)
            except User.DoesNotExist:
                pass

            user = form.save()
            user.refresh_from_db()
            user.customer.first_name = form.cleaned_data.get('first_name')
            user.customer.last_name = form.cleaned_data.get('last_name')
            user.customer.email = form.cleaned_data.get('email')

            user.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('core:home')
        else:
            self.get(request)
