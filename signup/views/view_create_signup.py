from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.views.generic import CreateView

from signup.forms import SignUpForm


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    success_message = "Usuário registrado com sucesso!"
    error_message = 'Não foi possível criar sua conta.'
    success_url = reverse_lazy('signup')
    template_name = 'registration/signup.html'

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)

    def form_valid(self, form):
        try:
            form.instance.is_active = False
            return super(SignUpView, self).form_valid(form)

        except IntegrityError:
            messages.add_message(self.request, messages.ERROR,
                                 'Não é possível inserir E-mail em duplicidade!')

            