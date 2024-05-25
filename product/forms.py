from django import forms
from autentification.models import CustomUser
from product.models import Products, Review, BatafsilMalumot


class GulForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price','image']


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment','star_given']


class BatafsilMalumotForm(forms.ModelForm):
    class Meta:
        model = BatafsilMalumot
        fields = ['first_name', 'phone']