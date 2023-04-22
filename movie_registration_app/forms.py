from django.forms import ModelForm
from movie_registration_app.models import Filmes


class FilmesForm(ModelForm):
    class Meta:
        model = Filmes
        fields = ['filme', 'ano', 'duracao', 'categoria', 'bilheteria']
