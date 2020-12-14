from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View

from authentication.forms import CustomerRegistrationForm


class UserRegistration(View):
    form = CustomerRegistrationForm
    template_name = 'registration/signup.html'

    def get(self, request):
        if request.user.is_authenticated: # этот метод тоже в ютилс можно
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
                pass # так нельзя делать

            user = form.save()
            user.refresh_from_db() # я не знаю правильно ли сначала обновлять бд, а потом дополнять инфу про юзера (вроде не так должно быть,но я огу ошибаться)
            user.customer.first_name = form.cleaned_data.get('first_name') 
            user.customer.last_name = form.cleaned_data.get('last_name')
            user.customer.email = form.cleaned_data.get('email')
            # if not customer.first_name or user.customer.last_name or user.customer.email => raise error 

            user.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password) # логика автоматической авторизации у тебя повторяется два раза точно, при смене пароля и при регестрации. Можно сделать файл utils.py в этой папке и запихнуть это, бо постоянное повторение кода выходит
            login(request, user)
            return redirect('core:home')
        else:
            self.get(request) # тут вообще не понимаю, почему в post-method идет get request, вроде тут ошибку нужно кинуть
