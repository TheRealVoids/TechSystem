import os

import dotenv
from mongoengine import connect

from apps.common.services.mongodb.models import (
    Products,
    RentalRequests,
    RequestedEquipments,
)

dotenv.load_dotenv()


def reset_database():
    Products.objects.delete()
    RentalRequests.objects.delete()
    print("Deleted all data from collections...")


def insert_data():

    Products.objects.create(
        category="Laptop",
        common_attributes={
            "brand": "Dell",
            "model": "XPS 15",
            "price": 1500.00,
            "stock": 10,
            "warranty_period": "2 years",
            "release_date": "2022-09-01",
        },
        specific_attributes={
            "processor": "Intel Core i7",
            "ram": "16 GB",
            "storage": "512 GB SSD",
            "graphics_card": "NVIDIA GeForce GTX 1650",
            "operating_system": "Windows 11",
        },
        image_url="https://m.media-amazon.com/images/I/91WgL3IbNIL.jpg",
    )

    Products.objects.create(
        category="Printer",
        common_attributes={
            "brand": "Canon",
            "model": "Pixma G6020",
            "price": 250.00,
            "stock": 25,
            "warranty_period": "1 year",
            "release_date": "2021-06-15",
        },
        specific_attributes={
            "printing_technology": "Inkjet",
            "connectivity_options": "Wi-Fi, USB",
        },
        image_url="https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6356/6356231_rd.jpg",
    )

    Products.objects.create(
        category="Tablet",
        common_attributes={
            "brand": "Samsung",
            "model": "Galaxy Tab S8",
            "price": 800.00,
            "stock": 30,
            "warranty_period": "1 year",
            "release_date": "2023-03-10",
        },
        specific_attributes={
            "screen_size": "11 inches",
            "battery_life": "12 hours",
            "camera_resolution": "13 MP",
            "operating_system": "Android",
        },
        image_url="https://specs-tech.com/wp-content/uploads/2021/06/Samsung-Galaxy-Tab-S8.jpg",
    )

    Products.objects.create(
        category="Smartphone",
        common_attributes={
            "brand": "Apple",
            "model": "iPhone 14 Pro",
            "price": 1200.00,
            "stock": 20,
            "warranty_period": "1 year",
            "release_date": "2022-09-15",
        },
        specific_attributes={
            "screen_size": "6.1 inches",
            "battery_life": "20 hours",
            "camera_resolution": "48 MP",
            "operating_system": "iOS",
        },
        image_url="https://mvdstore.uy/wp-content/uploads/2022/09/Apple-iPhone-14-Pro-iPhone.jpg",
    )

    print("Inserted Products data...")

    rental_requests_data = [
        {
            "customer_nit": "123456789",
            "requested_equipment": [
                {
                    "product_id": Products.objects.filter(
                        common_attributes__model="XPS 15"
                    )
                    .first()
                    .id,
                    "quantity": 2,
                },
                {
                    "product_id": Products.objects.filter(
                        common_attributes__model="Pixma G6020"
                    )
                    .first()
                    .id,
                    "quantity": 1,
                },
            ],
        },
        {
            "customer_nit": "987654321",
            "requested_equipment": [
                {
                    "product_id": Products.objects.filter(
                        common_attributes__model="Galaxy Tab S8"
                    )
                    .first()
                    .id,
                    "quantity": 3,
                },
            ],
        },
        {
            "customer_nit": "456123789",
            "requested_equipment": [
                {
                    "product_id": Products.objects.filter(
                        common_attributes__model="iPhone 14 Pro"
                    )
                    .first()
                    .id,
                    "quantity": 5,
                },
            ],
        },
    ]

    for request_data in rental_requests_data:
        requested_equipments = [
            RequestedEquipments(
                product_id=item["product_id"], quantity=item["quantity"]
            )
            for item in request_data["requested_equipment"]
        ]
        RentalRequests.objects.create(
            customer_nit=request_data["customer_nit"],
            requested_equipment=requested_equipments,
        )

    print("Inserted RentalRequests data...")


if __name__ == "__main__":
    connect(
        db=os.getenv("DB_NAME_MONGO"),
        host=os.getenv("DB_HOST_MONGO").replace(
            "<db_password>", os.getenv("DB_PASSWORD_MONGO")
        ),
        username=os.getenv("DB_USER_MONGO"),
        password=os.getenv("DB_PASSWORD_MONGO"),
        authentication_source="admin",
    )
    reset_database()
    insert_data()
