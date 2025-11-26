from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ScraperForm
from .utils import hacer_scraping, enviar_resultados_por_mail

class ScraperView(LoginRequiredMixin, FormView):
    template_name = 'scraper/form.html'
    form_class = ScraperForm
    success_url = reverse_lazy('scraper')

    login_url = 'login'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        keyword = form.cleaned_data['keyword']
        resultados = hacer_scraping(keyword)

        enviar_resultados_por_mail(resultados, self.request.user.email)

        return self.render_to_response(self.get_context_data(form=form, resultados=resultados))

    def form_invalid(self, form):
        print("❌ Formulario inválido")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
