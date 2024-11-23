from django.apps import AppConfig
from django.conf import settings
from mongoengine import connect


class MongodbConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.common.services.mongodb"

    def ready(self):
        initialize_mongo()


def initialize_mongo():
    connect(
        db=settings.MONGO_CONFIG["db"],
        host=settings.MONGO_CONFIG["host"],
        username=settings.MONGO_CONFIG.get("username"),
        password=settings.MONGO_CONFIG.get("password"),
        authentication_source=settings.MONGO_CONFIG.get(
            "authentication_source", "admin"
        ),
    )
