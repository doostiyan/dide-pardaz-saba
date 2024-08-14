from django import forms

from shop.models import Brand, Mobile


class CreateBrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = '__all__'


class CreateMobileForm(forms.ModelForm):

    class Meta:
        model = Mobile
        fields = '__all__'