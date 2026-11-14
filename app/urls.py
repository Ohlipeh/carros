# Import mod admin, panel adm.
from django.contrib import admin

# Import function path, use for link urls in page
from django.urls import path

# Import settings for read config my settings.py (MEDIA_URL and MEDIA_ROT)
from django.conf import settings

# Import function static, server filers ( send image p/ users)
from django.conf.urls.static import static

# Import register_view file accounts/views.py
from accounts.views import login_view, logout_view, register_view

# I import two new views, in its place the old.
from cars.views import CarListView, NewCarCreateView

# I create list urlpatterns, Django search which scription ledads where
urlpatterns = [
    # I speak scription "admin/" open panel admin for django.
    path("admin/", admin.site.urls),
    # I link the address "cars/" class CarListView: The as_view() transform class in a function w/ django can call.
    path("cars/", CarListView.as_view(), name="cars_list"),
    # I link the address "new_cr/" of class NewCarCreateView; the name="new_car" is the nickname use for call this route in templates.
    path("new_car/", NewCarCreateView.as_view(), name="new_car"),
    # I link the address "register/" the view register_view: the name="register" is of nick the use for call this route in templates.
    path("register/", register_view, name="register"),
    # I link the address "login/" the view login_view: the name="login" is nick what the redirect("login") use
    path("login/", login_view, name="login"),
    # I link the address "logout/" the view logout_view, with nick "logout"
    path("logout/", logout_view, name="logout"),
    # MEDIA_URL is scription public (ex: /media/) and MEDIA_ROOT is file real in computer menu.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
