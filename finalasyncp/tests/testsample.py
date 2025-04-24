import string
from tempfile import NamedTemporaryFile

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from upload_center.forms import UploadFileForm


def with_temp_file(empty=False):
    def decorator(func):
        def runner(*args, **kwargs):
            with NamedTemporaryFile() as f:
                f.write((string.printable * (0 if empty else 1)).encode('utf-8'))
                f.seek(0)
                temp_file = SimpleUploadedFile(f.name, f.read())
                func(*args, temp_file=temp_file, **kwargs)

        return runner

    return decorator


class TestAsyncUploader(TestCase):

    @with_temp_file()
    def test_valid_form(self, temp_file):
        form = UploadFileForm(data={'file_name': 'یک فایل'}, files={'file': temp_file})
        self.assertTrue(form.is_valid(), msg='\nتابع upload .شما، فایل‌های یک فرم معتبر را به درستی آپلود نمی‌کند')

    @with_temp_file()
    def test_form_invalid_name(self, temp_file):
        form = UploadFileForm(data={'file_name': 'یک'}, files={'file': temp_file})
        self.assertFalse(form.is_valid(), msg='\nتابع upload .شما، فایل‌های یک فرم نامعتبر را به درستی آپلود می‌کند')