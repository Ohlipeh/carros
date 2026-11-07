# I import the model forms django, that gives me tools for create forms.
from django import forms

# I import the model Brand for list the mark in camp choice.
from cars.models import Brand


# I create class CarForm; each variable within it becomes a field in the form.
class CarForm(forms.Form):
    # I create camp text model car.
    model = forms.CharField(max_length=200)
    # I create list the choice with all models.
    brand = forms.ModelChoiceField(Brand.objects.all())
    # I create camp accept number int.
    factory_year = forms.IntegerField()
    # I create camp accept number int
    model_year = forms.IntegerField()
    # I create camp text for plate.
    plate = forms.CharField(max_length=10)
    # I create a camp accept number with (decimal).
    value = forms.FloatField()
    # I create a camp for send a image.
    photo = forms.ImageField()
