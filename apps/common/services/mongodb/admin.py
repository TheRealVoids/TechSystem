from django.contrib import admin

from .models import Products, RentalRequests, RequestedEquipments, SpecificAttributes


class ProductsAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Products model.
    """

    list_display = [field.name for field in Products._meta.fields]
    search_fields = [
        "category",
        "image_url",
    ]  # Puedes añadir campos de búsqueda si lo deseas


class RentalRequestsAdmin(admin.ModelAdmin):
    """
    Admin configuration for the RentalRequests model.
    """

    list_display = ["customer_nit", "request_date", "status"]  # Los campos a mostrar
    list_filter = ["status"]  # Filtro por status
    search_fields = ["customer_nit"]  # Puedes añadir campos de búsqueda si lo deseas


class RequestedEquipmentsAdmin(admin.ModelAdmin):
    """
    Admin configuration for the RequestedEquipments model.
    """

    list_display = ["product_id", "quantity"]  # Los campos a mostrar
    search_fields = ["product_id"]


class SpecificAttributesAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SpecificAttributes model.
    """

    list_display = [
        "processor",
        "ram",
        "storage",
        "graphics_card",
        "operating_system",
        "printing_technology",
        "connectivity_options",
        "screen_size",
        "battery_life",
        "camera_resolution",
    ]  # Los campos a mostrar
    search_fields = [
        "processor",
        "ram",
        "storage",
    ]  # Puedes añadir campos de búsqueda si lo deseas


# Registramos los modelos en el panel de administración
admin.site.register(Products, ProductsAdmin)
admin.site.register(RentalRequests, RentalRequestsAdmin)
admin.site.register(RequestedEquipments, RequestedEquipmentsAdmin)
admin.site.register(SpecificAttributes, SpecificAttributesAdmin)
