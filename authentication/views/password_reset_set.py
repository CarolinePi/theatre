from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View


class PasswordResetSet(View):
    form = SetPasswordForm
    template_name = 'registration/password_reset_set.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:home')

        user = self.user_get(request)
        form = SetPasswordForm(user)
        context = {'form': form, 'messages': []}
        return render(request, self.template_name, context=context)

    def post(self, request):
        user = self.user_get(request)
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            password = form.cleaned_data.get('new_password1')
            user.set_password(password)
            user.save()

            return redirect('authentication:password-reset-done')
        else:
            messages = form.error_messages.values()

        context = {'form': self.form, 'messages': messages}
        return render(request, self.template_name, context=context)

    def user_get(self, request):
        email = request.session['email']
        user = User.objects.get(email=email) # не обработала ошибку, что нет юзера
        return user
