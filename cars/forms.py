# I import the model forms django, that gives me tools for create forms.
from django import forms

# I import the model Car, because the form to go is monted from her.
from cars.models import Car


# I create the class CarModelForm: come by from ModelForm allows Django to in only camps, read the model.
class CarModelForm(forms.ModelForm):
    # I create the class Meta, that keeps the config form.
    class Meta:
        # I will state which template serves as the basis for the form.
        model = Car
        # I will states which camps whitin in form: "__all__" means all fields of the model
        fields = "__all__"
