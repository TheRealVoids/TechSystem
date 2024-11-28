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
    # Define category IDs consistent with generate_postgres.py
    categories = {
        "Laptops": "CAT1",
        "Desktops": "CAT2",
        "Monitors": "CAT3",
        "Printers": "CAT4",
        "Tablets": "CAT5",
        "Mobile Phones": "CAT6",
        "Cameras": "CAT7",
        "Headphones": "CAT8",
    }

    Products.objects.create(
        category=categories["Laptops"],
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
        category=categories["Printers"],
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
        category=categories["Tablets"],
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
        category=categories["Mobile Phones"],
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

    Products.objects.create(
        category=categories["Cameras"],
        common_attributes={
            "brand": "Canon",
            "model": "EOS R5",
            "price": 3500.00,
            "stock": 15,
            "warranty_period": "1 year",
            "release_date": "2021-07-30",
        },
        specific_attributes={
            "resolution": "45 MP",
            "sensor_size": "Full Frame",
            "video_resolution": "8K",
        },
        image_url="https://i1.adis.ws/i/canon/4147C025_EOS-R5_Position-1_02/product-front-view-with-lens?w=1500&bg=gray95",
    )

    Products.objects.create(
        category=categories["Headphones"],
        common_attributes={
            "brand": "Sony",
            "model": "WH-1000XM4",
            "price": 350.00,
            "stock": 50,
            "warranty_period": "1 year",
            "release_date": "2020-08-06",
        },
        specific_attributes={
            "noise_cancellation": "Active",
            "battery_life": "30 hours",
            "connectivity_options": "Bluetooth 5.0",
        },
        image_url="https://mspoweruser.com/wp-content/uploads/2020/08/Sony-WH-1000XM4.jpg",
    )

    # Additional products
    Products.objects.create(
        category=categories["Laptops"],
        common_attributes={
            "brand": "HP",
            "model": "Spectre x360",
            "price": 1400.00,
            "stock": 15,
            "warranty_period": "2 years",
            "release_date": "2021-10-01",
        },
        specific_attributes={
            "processor": "Intel Core i7",
            "ram": "16 GB",
            "storage": "1 TB SSD",
            "graphics_card": "Intel Iris Xe",
            "operating_system": "Windows 10",
        },
        image_url="https://th.bing.com/th/id/OIP.1UkP3s33jysdodsBnjiMHgHaFj?w=215&h=180&c=7&r=0&o=5&dpr=1.1&pid=1.7",
    )

    Products.objects.create(
        category=categories["Desktops"],
        common_attributes={
            "brand": "Apple",
            "model": "iMac 24-inch",
            "price": 1800.00,
            "stock": 10,
            "warranty_period": "1 year",
            "release_date": "2021-05-21",
        },
        specific_attributes={
            "processor": "Apple M1",
            "ram": "8 GB",
            "storage": "256 GB SSD",
            "graphics_card": "Integrated",
            "operating_system": "macOS",
        },
        image_url="https://res.cloudinary.com/aeropost-inc/image/upload/live/PG59J0/PG59J03e1a-16844101428180-0",
    )

    Products.objects.create(
        category=categories["Monitors"],
        common_attributes={
            "brand": "LG",
            "model": "UltraFine 5K",
            "price": 1300.00,
            "stock": 20,
            "warranty_period": "1 year",
            "release_date": "2020-11-15",
        },
        specific_attributes={
            "screen_size": "27 inches",
            "resolution": "5120 x 2880",
        },
        image_url="https://cdn.wccftech.com/wp-content/uploads/2016/12/LG-UltraFine-5K-1.jpg",
    )

    Products.objects.create(
        category=categories["Printers"],
        common_attributes={
            "brand": "HP",
            "model": "LaserJet Pro MFP",
            "price": 400.00,
            "stock": 30,
            "warranty_period": "1 year",
            "release_date": "2021-02-10",
        },
        specific_attributes={
            "printing_technology": "Laser",
            "connectivity_options": "Wi-Fi, Ethernet, USB",
        },
        image_url="https://www.bhphotovideo.com/images/images2500x2500/hp_2z619f_laserjet_pro_mfp_4101fdw_1716842.jpg",
    )

    Products.objects.create(
        category=categories["Tablets"],
        common_attributes={
            "brand": "Apple",
            "model": "iPad Pro",
            "price": 1000.00,
            "stock": 25,
            "warranty_period": "1 year",
            "release_date": "2021-04-30",
        },
        specific_attributes={
            "screen_size": "12.9 inches",
            "battery_life": "10 hours",
            "camera_resolution": "12 MP",
            "operating_system": "iPadOS",
        },
        image_url="https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/refurb-ipad-pro-11-wifi-silver-2019?wid=1144&hei=1144&fmt=jpeg&qlt=80&op_usm=0.5,0.5&.v=1581985473264",
    )

    Products.objects.create(
        category=categories["Mobile Phones"],
        common_attributes={
            "brand": "Samsung",
            "model": "Galaxy S21",
            "price": 999.00,
            "stock": 40,
            "warranty_period": "1 year",
            "release_date": "2021-01-29",
        },
        specific_attributes={
            "screen_size": "6.2 inches",
            "battery_life": "18 hours",
            "camera_resolution": "64 MP",
            "operating_system": "Android",
        },
        image_url="https://th.bing.com/th/id/OIP.Ojv_cKQXK-TCohfc51cEdgHaHa?rs=1&pid=ImgDetMain",
    )

    Products.objects.create(
        category=categories["Cameras"],
        common_attributes={
            "brand": "Nikon",
            "model": "Z6 II",
            "price": 2000.00,
            "stock": 20,
            "warranty_period": "1 year",
            "release_date": "2020-10-14",
        },
        specific_attributes={
            "resolution": "24.5 MP",
            "sensor_size": "Full Frame",
            "video_resolution": "4K",
        },
        image_url="https://th.bing.com/th/id/OIP.T2AXQ74viu4ZA0JWn_LyuAHaGC?rs=1&pid=ImgDetMain",
    )

    Products.objects.create(
        category=categories["Headphones"],
        common_attributes={
            "brand": "Bose",
            "model": "QuietComfort 35 II",
            "price": 300.00,
            "stock": 35,
            "warranty_period": "1 year",
            "release_date": "2019-09-05",
        },
        specific_attributes={
            "noise_cancellation": "Active",
            "battery_life": "20 hours",
            "connectivity_options": "Bluetooth 4.1",
        },
        image_url="https://th.bing.com/th/id/OIP.hsFJ-FY3zm2zdgejV5AmTAAAAA?rs=1&pid=ImgDetMain",
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
