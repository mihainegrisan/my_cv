from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices = PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)
    update = forms.BooleanField(required=False,
                                 initial=False,
                                 widget=forms.HiddenInput)
    # 'updated' indicates whether the quantity has to
    # be added to any existing quantity in the cart for this product
    # (False), or whether the existing quantity has to be updated
    # with the given quantity (True).
