from django import forms
from autentification.models import CustomUser
from product.models import GulProduct, Review, BatafsilMalumot


class GulForm(forms.ModelForm):
    class Meta:
        model = GulProduct
        fields = ['name', 'price','image']


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment','star_given']

class BatafsilMalumotForm(forms.ModelForm):
    class Meta:
        model = BatafsilMalumot
        fields = ['first_name', 'phone']