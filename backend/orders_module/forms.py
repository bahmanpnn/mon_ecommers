from django import forms


class AddBasketForm(forms.Form):
    quantity=forms.IntegerField(min_value=1,max_value=30)

class CouponApplyForm(forms.Form):
    code=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control col-md-1'
    }))