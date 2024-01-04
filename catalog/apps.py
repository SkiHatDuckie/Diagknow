from django.apps import AppConfig
from django.db.models.signals import post_save

class CatalogConfig(AppConfig):
    name = 'catalog'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        from django.db import models  # HERE IT IS! MOVING THE IMPORT HERE SOLVED IT
        #post_save.connect(my_receiver, sender=MyModel)