from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomerCreationForm

class SignUpView(CreateView):
    form_class = CustomerCreationForm
    success_url = reverse_lazy("homepage")
    template_name = "registration/signup.html"