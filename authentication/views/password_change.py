from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View


class PasswordChangeView(View, LoginRequiredMixin):
    form = PasswordChangeForm

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('authentication:login')

        form = self.form(request.user)
        context = {'form': form, 'messages': []}
        return render(request, 'registration/password_change_form.html', context=context)

    def post(self, request):
        messages = []
        form = self.form(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data.get('new_password1') # Я хз валидируется ли на фронте эта штука, но тут может отдать None, если придет пустео поле
            if password:
                user.set_password(password)
                user.save()

                user = authenticate(username=user.username, password=password)
                login(request, user)
                return redirect('core:home')
            else:
                messages = ['password is None']
        else:
            messages = list(form.error_messages.values())
            
        form = self.form(request.user)
        context = {'form': form, 'messages': messages}
        return render(request, 'registration/password_change_form.html', context=context)
