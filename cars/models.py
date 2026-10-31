from django.db import models


# Create class Car
class Car(models.Model):
    # AutoField = AutoIncremento
    id = models.AutoField(primary_key=True)
    # CharField = String, max_length = Max character
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    # IntegerField = Number Int, blank=True = want white, null=True = want nullo
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    # FloatField = Point Float
    value = models.FloatField(blank=True, null=True)

    def __str__(self):
        # Remove "Car object 2" and customize with the name of the object.
        return self.model
