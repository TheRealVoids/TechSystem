import datetime

from mongoengine import (
    DateTimeField,
    DictField,
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    EmbeddedDocumentListField,
    IntField,
    ObjectIdField,
    StringField,
    URLField,
)


class SpecificAttributes(EmbeddedDocument):
    # Attributes for laptops and desktops
    processor = StringField(max_length=100)
    ram = StringField(max_length=50)
    storage = StringField(max_length=100)
    graphics_card = StringField(max_length=100)
    operating_system = StringField(max_length=100)

    # Attributes for printers
    printing_technology = StringField(max_length=100)
    connectivity_options = StringField(max_length=100)

    # Attributes for tablets and smartphones
    screen_size = StringField(max_length=50)
    battery_life = StringField(max_length=50)
    camera_resolution = StringField(max_length=50)

    # Attributes for cameras
    resolution = StringField(max_length=50)
    sensor_size = StringField(max_length=50)
    video_resolution = StringField(max_length=50)

    # Attributes for headphones
    noise_cancellation = StringField(max_length=50)
    connectivity_options = StringField(max_length=100)
    battery_life = StringField(max_length=50)


class Products(Document):
    category = StringField(max_length=50, required=True)  # e.g., 'Laptop', 'Printer'
    common_attributes = DictField()  # Common attributes as JSON
    specific_attributes = EmbeddedDocumentField(
        SpecificAttributes
    )  # Embedded dynamic attributes
    image_url = URLField()


class RequestedEquipments(EmbeddedDocument):
    product_id = ObjectIdField()  # Reference to Product
    quantity = IntField(min_value=1)


class RentalRequests(Document):
    customer_nit = StringField(max_length=20, required=True)
    request_date = DateTimeField(default=datetime.datetime.utcnow)
    status = StringField(
        choices=["pending", "approved", "rejected"], default="pending", max_length=20
    )
    requested_equipment = EmbeddedDocumentListField(
        RequestedEquipments
    )  # List of requested products
