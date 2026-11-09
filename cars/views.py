# I import function render, that takes a file HTML (template) and the transforme in a page browser.
from django.shortcuts import redirect, render

# I import cars models in Car, The view need use model.
from cars.models import Car
from cars.forms import CarModelForm


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


# I create view new_car_view, which shows the registration page for a new car.
def new_car_view(request):
    # I verefications if order is a send the forms (POST).
    if request.method == "POST":
        # I create the form already filled: request.POST contains text and numbers, while request.FILES contains files (the photo).
        new_car_form = CarModelForm(request.POST, request.FILES)
        # I verifications are if all the camps valid (mandatory camps   filled, correct numbers, image valid).
        if new_car_form.is_valid():
            # I call the save() of created in CarForm for record the car in bank.
            new_car_form.save()
            # I direct for the list of cars, used the nick the route cars_list.
            return redirect("cars_list")
    # I used the else for where the order is GET (the person just open page).
    else:
        # I create a form CarModelForm empty, ready to be filled out.
        new_car_form = CarModelForm()
    # I return page new_car.html and send the form whithin at in dict.
    return render(request, "new_car.html", {"new_car_form": new_car_form})
