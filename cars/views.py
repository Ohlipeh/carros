from django.http import HttpResponse


# Create my views here.
def cars_view(request):
    return HttpResponse("Meus carros")
