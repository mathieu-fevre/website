from django.contrib import admin
from django.apps import apps

app_config = apps.get_app_config("homm3")

for model in app_config.get_models():
    admin.site.register(model)