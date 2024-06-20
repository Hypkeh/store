from django import forms
from django.forms import ModelForm
from .models import Product
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    q = forms.CharField(max_length=20, label='Поиск по словам')


class ProductForm(ModelForm):
    category = forms.CharField(label='Категория продукта')
    expires = forms.IntegerField(label='Срок годности продукта')
    

    class Meta:
        model = Product
        fields = '__all__'


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', required=False, widget=forms.widgets.PasswordInput())
    password2 = forms.CharField(label='Пароль (повторно)', initial='начальное значение', required=False)
    regex_field = forms.RegexField(r'^U[a-zA-Z]{4}$')
    is_client = forms.BooleanField()
 #   rate = forms.FloatField()
 #   number_of_goods = forms.IntegerField(widget=forms.widgets.NumberInput())
 #   desired_date = forms.DateField(widget=forms.widgets.DateInput())
 #   choice = forms.ChoiceField(choices=(('f', 'first'), ('s', 'second')))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)