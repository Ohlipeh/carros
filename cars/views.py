# I import function render, that takes a file HTML (template) and the transforme in a page browser.
from django.shortcuts import render

# I import cars models in Car, The view need use model.
from cars.models import Car


# I write here the my views, that are fuctions that decides what appears when someone acesses an address.
# I create the fuction cars_view; the parameter request saved everything regarding the request made by the browser
def cars_view(request):
    # In my objects Car i want all. (SQL 'Querys'). order_by sort in "ABC" order.
    cars = Car.objects.all().order_by("model")
    # before verification if user performed a search.
    search = request.GET.get("search")
    if search:
        cars = Car.objects.filter(model__icontains=search)
    # I'll return it as the response the page cars.html, used the render it request to set everything up just right.
    return render(request, "cars.html", {"cars": cars})
