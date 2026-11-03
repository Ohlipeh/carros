# I import function render, that takes a file HTML (template) and the transforme in a page browser.
from django.shortcuts import render

# I import cars models in Car, The view need use model.
from cars.models import Car


# I write here the my views, that are fuctions that decides what appears when someone acesses an address.
# I create the fuction cars_view; the parameter request saved everything regarding the request made by the browser
def cars_view(request):
    # In my objects Car i want all. (SQL 'Querys')
    cars = Car.objects.all()
    # I'll return it as the response the page cars.html, used the render it request to set everything up just right.
    return render(request, "cars.html", {"cars": cars})
