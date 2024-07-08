from django.contrib import admin

from .models import TransientHouseLocations, TransientHouse, Owner, RoomSpecifiction, Room

admin.site.register(TransientHouse)
admin.site.register(TransientHouseLocations)
admin.site.register(Owner)
admin.site.register(RoomSpecifiction)
admin.site.register(Room)




