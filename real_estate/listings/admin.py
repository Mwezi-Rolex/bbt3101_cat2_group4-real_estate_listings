from django.contrib import admin
from .models import Agent, Property, Client, Booking, PropertyImage  # import your models

admin.site.register(Agent)
admin.site.register(Property)
admin.site.register(Client)
admin.site.register(Booking)
admin.site.register(PropertyImage)
