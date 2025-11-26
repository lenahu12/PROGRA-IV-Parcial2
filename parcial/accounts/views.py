# accounts/views.py
from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import SignUpForm

class SignUpView(FormView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        try:
            sent = send_mail(
                subject='Bienvenido a la plataforma',
                message=f'Gracias por registrarte, {user.username}.',
                from_email=None,
                recipient_list=[user.email],
                fail_silently=False,
            )
            print(f"Correo de bienvenida enviado a {user.email}. Resultado: {sent}")
        except Exception as e:
            print(f"Error al enviar correo: {e}")
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = 'home'  