# I import function render, the transforms a templates HTML in a page.
from django.shortcuts import render

# I import the UserCreationForm, a form ready the django for create user.
from django.contrib.auth.forms import UserCreationForm


# I create the view register_view, which the page shows cadaster of user.
def register_view(request):
    # I create a form empty the cadaster the user.
    user_form = UserCreationForm()
    # I return the page register.html and send the form within the a dict.
    return render(request, "register.html", {"user_form": user_form})
