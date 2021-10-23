from django.forms import ModelForm
from .models import BookModel


class BookForm(ModelForm):
    class Meta:
        model = BookModel
        fields = ('id', 'name', 'contact', 'email',
                  'doctor', 'message', 'time', 'date')
