from django.forms import ModelForm, CharField
from .models import Reseni

class ReseniForm(ModelForm):
    def __init__(self, *args, priklad, **kwargs):
            super(ReseniForm, self).__init__(*args, **kwargs)
            self.fields["reseni"] = CharField(max_length=200, required=False)

    class Meta:
        model = Reseni
        fields = ('reseni',)