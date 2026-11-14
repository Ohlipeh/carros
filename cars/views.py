# I import two views generic ready: ListView (shows a list the obj) and CreateView (show the process a form the create)
from django.views.generic import CreateView, ListView

# I import cars models in Car, The view need use model.
from cars.models import Car

# I import the form CarModelForm, what created from model Car
from cars.forms import CarModelForm


# I create class CarsListView: Inherit  the ListView make django fetch it obj and put together the list on my own
class CarListView(ListView):
    # I specify which model the list will display
    model = Car
    # I specify which HTML template will be used to display the list
    template_name = "cars.html"
    # I specify the name of the variable that the HTML will receive (the {% for car in cars %} uses this name)
    context_object_name = "cars"

    # I overrode get_queryset, which is the method that decides WHICH cars are included in the list
    def get_queryset(self):
        # I call the original get_queryset (which returns all cars) using super() and sort by model (A to Z)
        cars = super().get_queryset().order_by("model")
        # I retrieve the search text from the URL; within the class, the request is stored in self.request
        search = self.request.GET.get("search")
        # I verific if exists some text the search
        if search:
            # I filter the list is which already order, ignored MAX and MIN
            cars = cars.filter(model_icontains=search)
        # I return the list end the cras
        return cars


# I create the class NewCreateView: Inherit the CreateView aready the django to take car alone
class NewCarCreateView(CreateView):
    # I specify which model is to go create.
    model = Car
    # I specify which form used
    form_class = CarModelForm
    # I specify which HTML template will be form
    template_name = "new_car.html"
    # I specify for from the person will be after save with sucess
    success_url = "/cars/"
