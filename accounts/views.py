# I import function render, the transforms a templates HTML in a page.
from django.shortcuts import redirect, render

# I import the UserCreationForm, a form ready the django for create user.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# I create the view register_view, which the page shows cadaster of user.
def register_view(request):
    # I verificate if the person send the form (POST)
    if request.method == "POST":
        # I create form ready pre. with send data
        user_form = UserCreationForm(request.POST)
        # I verificate if the data are valid (user, password equal and strong)
        if user_form.is_valid():
            # I saved a new user in data:the django save the password criptografada.
            user_form.save()
            # I return the person for page login.
            return redirect("login")
    # I use the else for which the person also open the page (GET)
    else:
        # I create a form empty the cadaster the user.
        user_form = UserCreationForm()
        # I return the page register.html and send the form within the a dict.
    return render(request, "register.html", {"user_form": user_form})


# I create a view login_view, which showa process login
def login_view(request):
    # I verificate if person send o form (POST)
    if request.method == "POST":
        # I take user writer: request.POST is the dict with the data send
        username = request.POST["username"]
        # I take the password writer
        password = request.POST["password"]
        # I check user and password: if they are right return user, and is not return None
        user = authenticate(request, username=username, password=password)
        # I verificate if login it worked out
        if user is not None:
            # I open the user session, and from here the django do you know who he is
            login(request, user)
            # I return person for the list cars.
            return redirect("cars_list")
        # I use the else for which user or password are wrong.
        else:
            # I create form login empty for try again.
            login_form = AuthenticationForm()
    # I use the else for which the person also open the page (GET)
    else:
        # I create the form login empty
        login_form = AuthenticationForm()
    # I return the page login.html with the form
    return render(request, "login.html", {"login_form": login_form})


# I create the view logout_view, which concludes the session
def logout_view(request):
    # I concludes the session the current user
    logout(request)
    # I return the person back the list cars
    return redirect("cars_list")
