from django import forms
from .models import *


# >>>>>>> HOME PAGE <<<<<<<<<
class HomeContentForm(forms.ModelForm):
    class Meta:
        model = HomeContent
        fields = ['title', 'content', 'image']


# >>>>>>>>> STORE PAGE <<<<<<<<<<
class StoreProductsForm(forms.ModelForm):
    class Meta:
        model = StoreProducts
        fields = ['image', 'name_product', 'incomplete_description', 'continue_description', 'price']


option = (('1', 'A - Z'),
          ('2', 'Z - A'),
          ('3', 'Cena wgóre'),
          ('4', 'Cena wdół'),)


class SortedForm(forms.Form):
    sorted_prod = forms.ChoiceField(choices=option, label='')


class PriceMinMax(forms.Form):
    price_min = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "price"}), min_value=0, max_value=99999)
    price_max = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "price"}), min_value=1, max_value=100000)


class SearchForm(forms.Form):
    search_prod = forms.CharField(widget=forms.TextInput(attrs={"class": "search", 'placeholder': 'czego szukasz?'}),
                                  max_length="20", label='')


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
        fields = ['image', 'title', 'content', 'author']


# >>>>>>>>> CONTACT PAGE <<<<<<<<<<<
class ContactDataForm(forms.ModelForm):
    class Meta:
        model = ContactData
        fields = ['address', 'telephone', 'facebook']


class WorkingHoursForm(forms.ModelForm):
    class Meta:
        model = WorkingHours
        fields = ['working_day', 'working_hours']
