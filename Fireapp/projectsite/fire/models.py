from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TransientHouseLocations(BaseModel):
    name = models.CharField(max_length=150)
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150) 
    country = models.CharField(max_length=150)

class Owner(BaseModel):
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150)
    contact_information = models.CharField(max_length=150)

class TransientHouse(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    location = models.OneToOneField(TransientHouseLocations, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class RoomSpecifiction(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Room(models.Model):
    transient_house = models.ForeignKey(TransientHouse, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    specification = models.ForeignKey(RoomSpecifiction, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.transient_house.name} - {self.name}"

