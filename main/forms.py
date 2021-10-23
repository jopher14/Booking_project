from django import forms
from booking.models import BookModel


class bookForms(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ('id', 'name', 'contact', 'email',
                  'doctor', 'message', 'time', 'date')
