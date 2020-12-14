from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View


class PasswordResetView(View):
    form = PasswordResetForm
    template_name = 'registration/password_reset_form.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('authentication:password-change')

        context = {'form': self.form, 'messages': []}
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email') # Та же херня, .get() возвратит None, если в form.cleaned_data не будет email
            try:
                User.objects.get(email=email)
            except User.DoesNotExist:
                context = {'form': self.form, 'messages': ['User with this email doesn\'t exists.']}
                return render(request, self.template_name, context=context)

            request.session['email'] = email
            return redirect(reverse('authentication:password-reset-set'))
        messages = ["you have entered invalid information"]
        context = {'form': self.form, 'messages': messages}
        return render(request, self.template_name, context=context)
