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

    # I valid in camp "value": Django calls this method on its own because the name follows the pattern clean_ + field name
    def clean_value(self):
        # I'll take a value the person provided, ready convert for number, in dict cleaned_data
        value = self.cleaned_data.get("value")
        # I verific if the value is < the 20000
        if value < 20000:
            # I add a ensage the error in cap "value", that appears on the form
            self.add_error("value", "The minimum value of the car must be $20.000.")
        # I return the value: All metod clean_ need finish data.
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get("factory_year")
        if factory_year < 1970:
            self.add_error(
                "factory_year",
                "It is not possible to register cars manufactured before 1975.",
            )
        return factory_year

    def clean_photo(self):
        photo = self.cleaned_data.get("photo")
        if photo == None:
            self.add_error("photo", "You need to add an image!")
        return photo
