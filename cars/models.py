from django.db import models


# New class
class Brand(models.Model):
    # Primary key brand id.
    id = models.AutoField(primary_key=True)
    # name in table.
    name = models.CharField(max_length=200)

    def __str__(self):
        # Remove "Car object 2" and customize with the name of the object.
        return self.name


# Create class Car
class Car(models.Model):
    # AutoField = AutoIncremento.
    id = models.AutoField(primary_key=True)
    # CharField = String, max_length = Max character.
    model = models.CharField(max_length=200)
    # ForeignKey = link to another table 'Brand', on_delete= Mod protect, related_name = relation name.
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand")
    # IntegerField = Number Int, blank=True = want white, null=True = want nullo.
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    # FloatField = Point Float.
    value = models.FloatField(blank=True, null=True)
    # ImageField = Image in file, upload_to = upload in file "cars"
    photo = models.ImageField(upload_to="cars/", blank=True, null=True)

    def __str__(self):
        # Remove "Car object 2" and customize with the name of the object.
        return self.model
