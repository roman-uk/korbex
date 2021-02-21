from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User


#        Login Form
class LoginForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


# Change password Form
class UpdatePasswordForm(PasswordChangeForm, SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #  rewrite error message
        self.error_messages['password_incorrect'] = "Twoje stare hasło zostało wprowadzone nieprawidłowo. Proszę wprowadzić ponownie."
        self.error_messages['password_mismatch'] = "Dwa pola hasła nie pasowały"
        self.fields["old_password"].label = "Stare hasło"
        self.fields["new_password1"].label = "Nowe hasło "
        self.fields["new_password2"].label = "Powtórz nowe hasło "


# >>>>>>> HOME PAGE <<<<<<<<<
class HomeContentForm(forms.ModelForm):
    class Meta:
        model = HomeContent
        fields = ['title', 'content', 'image']

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Tytuł artykułu',
                'style': 'width: 300px'
            }),
            'content': forms.Textarea(attrs={
                'cols': 80, 'rows': 20,
                'placeholder': 'Treść artykułu',
                'style': 'font-size: 14px'
            })
        }


# >>>>>>>>> STORE PAGE <<<<<<<<<<
class StoreProductsForm(forms.ModelForm):
    class Meta:
        model = StoreProducts
        fields = ['name_product', 'image', 'incomplete_description', 'continue_description', 'price']

        widgets = {
            'name_product': forms.TextInput(attrs={
                'placeholder': 'Wpisz nazwę towaru'
            }),
            'incomplete_description': forms.Textarea(attrs={
                'placeholder': 'Napisz krótki opis towaru do 180 znaków',
                'cols': 30, 'rows': 5,
            }),
            'continue_description': forms.Textarea(attrs={
                'placeholder': 'Podaj pełny opis towaru',
                'cols': 60, 'rows': 15
            }),
        }


# >>>>>>>>> SERVICE PAGE <<<<<<<<<<<
class TypeRepairForm(forms.ModelForm):
    class Meta:
        model = TypeRepair
        fields = ['type_repair']

        widgets = {
            "type_repair": forms.TextInput(attrs={
                'class': "types_repair",
                'placeholder': 'Rodzaj naprawy'
            })
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name_repair', 'type_repair', 'price']


# >>>>>>>>>> BLOG PAGE <<<<<<<<<<<<
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'image']

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Tytul artyklu'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Treść artykułu'
            }),
            'author': forms.TextInput(attrs={
                'placeholder': 'Wprowadż ime awtora artykłu'
            })
        }


# >>>>>>>>> CONTACT PAGE <<<<<<<<<<<
class ContactDataForm(forms.ModelForm):
    class Meta:
        model = ContactData
        fields = ['address', 'telephone', 'facebook']


class WorkingHoursForm(forms.ModelForm):
    class Meta:
        model = WorkingHours
        fields = ['working_day', 'working_hours']
        widgets = {
            'working_hours': forms.TextInput(attrs={
                'placeholder': '8:00 - 18:00, albo Zamknięto'
            })
        }
