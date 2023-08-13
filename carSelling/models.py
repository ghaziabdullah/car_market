from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Registration(models.Model):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name
    
class BodyType(models.Model):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Car(models.Model):
    image = models.ImageField( null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(null=True, max_length=100)
    engine_capacity = models.IntegerField()
    registered_in = models.ForeignKey(Registration, on_delete=models.CASCADE)
    assembly = models.CharField(max_length=10, choices=[('Local', 'Local'),('Imported', 'Imported'),])
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE)
    make_year =  models.IntegerField()
    milage =  models.IntegerField()
    transmission =  models.CharField(max_length=10, choices=[('Automatic', 'Automatic'),('Manual', 'Manual'),])
    price = models.IntegerField()
    location = models.CharField(max_length=200, null=True)