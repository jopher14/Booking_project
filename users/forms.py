from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import ImageField
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('Save', 'Register'))
        self.helper.add_input(
            Submit('cancel', 'Cancel', css_class='btn btn-danger'))

        self.helper.layout = Layout(
            Row(
                Column('username'),
                Column('email'),
            ),
            Row(
                Column('password1'),
                Column('password2')
            )
        )


class ProfileUpdateForm(forms.ModelForm):
    image = ImageField()

    class Meta:
        model = Profile
        fields = ['image']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    contact = forms.CharField()

    class Meta:
        model = Profile
        db_table = "profile"
        fields = ['first_name', 'last_name', 'email', 'contact']
