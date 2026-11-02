# Import mod admin, panel adm.
from django.contrib import admin

# Import function path, use for link urls in page
from django.urls import path

# Import settings for read config my settings.py (MEDIA_URL and MEDIA_ROT)
from django.conf import settings

# Import function static, server filers ( send image p/ users)
from django.conf.urls.static import static

# Import cars_view file cars/views.py
from cars.views import cars_view

# I create list urlpatterns, Django search which scription ledads where
urlpatterns = [
    # I speak scription "admin/" open panel admin for django.
    path("admin/", admin.site.urls),
    path("cars/", cars_view),
    # MEDIA_URL is scription public (ex: /media/) and MEDIA_ROOT is file real in computer menu.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
