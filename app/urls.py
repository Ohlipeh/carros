# Import mod admin, panel adm.
from django.contrib import admin

# Import function path, use for link urls in page
from django.urls import path

# Import settings for read config my settings.py (MEDIA_URL and MEDIA_ROT)
from django.conf import settings

# Import function static, server filers ( send image p/ users)
from django.conf.urls.static import static

# Import register_view file accounts/views.py
from accounts.views import register_view

# Import cars_view file cars/views.py
from cars.views import cars_view, new_car_view

# I create list urlpatterns, Django search which scription ledads where
urlpatterns = [
    # I speak scription "admin/" open panel admin for django.
    path("admin/", admin.site.urls),
    path("cars/", cars_view, name="cars_list"),
    # I link the address "new_cr/" of view new_car_view; the name="new_car" is the nickname use for call this route in templates.
    path("new_car/", new_car_view, name="new_car"),
    # I link the address "register/" the view register_view: the name="register" is of nick the use for call this route in templates.
    path("register/", register_view, name="register"),
    # MEDIA_URL is scription public (ex: /media/) and MEDIA_ROOT is file real in computer menu.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
