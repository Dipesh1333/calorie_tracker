# django imports
from django.apps import AppConfig


class CalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cal_app'

    def ready(self):
    	import cal_app.signals
