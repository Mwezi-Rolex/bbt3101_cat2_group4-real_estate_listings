from django.contrib import admin
from .models import Agent, Property, Client, Booking, PropertyImage, PropertyType


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "agency", "license_number")
    search_fields = ("name", "email", "agency", "license_number")


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "location", "property_type", "agent", "date_listed")
    search_fields = ("title", "location", "agent__name", "property_type__name")
    list_filter = ("property_type", "agent", "date_listed")
    inlines = [PropertyImageInline]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
    search_fields = ("name", "email")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("client", "property", "status", "date_sent")
    search_fields = ("client__name", "property__title")
    list_filter = ("status", "date_sent")
