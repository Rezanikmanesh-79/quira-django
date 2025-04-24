import os

from django.apps import AppConfig
from django.conf import settings


class UploadCenterConfig(AppConfig):
    name = 'upload_center'

    def ready(self):
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
