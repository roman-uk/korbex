from django import forms


option = (('1', 'A - Z'),
          ('2', 'Z - A'),
          ('3', 'Cena wgóre'),
          ('4', 'Cena wdół'),
          )


class SortedForm(forms.Form):
    sorted_prod = forms.ChoiceField(choices=option, label='')


class PriceMinMax(forms.Form):
    price_min = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "price"}), min_value=0, max_value=99999)
    price_max = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "price"}), min_value=1, max_value=100000)


class SearchForm(forms.Form):
    search_prod = forms.CharField(widget=forms.TextInput(attrs={"class": "search", 'placeholder': 'czego szukasz?'}),
                                  max_length="20", label='')

