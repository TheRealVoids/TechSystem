from mongoengine import connect

from apps.common.services.mongodb.models import Products

connect(
    db="TechSystem",
    host="mongodb+srv://myAtlasDBUser:n4zm7KCFbUuFUysB@myatlasclusteredu.zr2tc.mongodb.net/",
    username="myAtlasDBUser",
    password="n4zm7KCFbUuFUysB",
    authentication_source="admin",
)

# Inserción de laptops
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

# Inserción de impresoras
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

# Inserción de tablets
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

# Inserción de smartphones
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
