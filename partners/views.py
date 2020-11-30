from django.views.generic import FormView, ListView

from partners.form import MovieForm
from partners.models import Movie


class MovieCreateView(FormView):
    template_name = 'form.html'
    form_class = MovieForm

