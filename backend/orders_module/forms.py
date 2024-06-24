from django import forms


class AddBasketForm(forms.Form):
    quantity=forms.IntegerField(min_value=1,max_value=30)