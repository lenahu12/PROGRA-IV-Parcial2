from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Alumno
from .utils import generar_pdf_alumno
from .forms import AlumnoForm

#vista basada en clase, en vez de usar login_required uso LoginReqruiedMixin
class DashboardView(LoginRequiredMixin, ListView):
    model = Alumno
    template_name = 'alumnos/dashboard.html'
    context_object_name = 'alumnos'

    def get_queryset(self):
        return Alumno.objects.filter(usuario=self.request.user)

class AlumnoCreateView(LoginRequiredMixin, CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumnos/alumno_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
#vista basada en función para usar @login_required como solicita la consigna.

@login_required
def enviar_pdf(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk, usuario=request.user)
    pdf_buffer = generar_pdf_alumno(alumno)
    destinatarios = [request.user.email, alumno.email]

    email = EmailMessage(
        subject=f"Ficha del alumno {alumno.nombre}",
        body="Adjunto encontrarás el PDF con los datos del alumno.",
        from_email=None, 
        to=destinatarios,  
    )
    email.attach(f"alumno_{alumno.pk}.pdf", pdf_buffer.read(), "application/pdf")
    email.send()

    print(f"PDF enviado a: {', '.join(destinatarios)}")
    return redirect('dashboard')