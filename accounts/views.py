# I import function render, the transforms a templates HTML in a page.
from django.shortcuts import redirect, render

# I import the UserCreationForm, a form ready the django for create user.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# I create the view register_view, which the page shows cadaster of user.
def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("login")
    else:
        # I create a form empty the cadaster the user.
        user_form = UserCreationForm()
        # I return the page register.html and send the form within the a dict.
    return render(request, "register.html", {"user_form": user_form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("cars_list")
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, "login.html", {"login_form": login_form})


def logout_view(request):
    logout(request)
    return redirect("cars_list")
