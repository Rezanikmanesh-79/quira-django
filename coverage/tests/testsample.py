import subprocess

from django.test import TestCase


def copy_content(from_, to_):
    def wrapper(test_func):
        def decorator(*args, **kwargs):
            with open(from_) as f:
                with open(to_, "w") as f1:
                    f1.write(f.read())
            test_func(*args, **kwargs)

        return decorator

    return wrapper


def empty_file(file_path):
    open(file_path, "w").close()


def extract_coverage_percent(coverage_report, file_path):
    coverage_report = coverage_report.decode("utf-8").split('\n')
    return int(next(filter(lambda x: file_path in x, coverage_report)).split()[-1].replace('%', '').strip())


class TestAll(TestCase):

    @copy_content("library_management/temp_tests_file.py", "library_management/tests.py")
    def test_coverage(self):
        subprocess.check_output("coverage run --source='.' manage.py test library_management", shell=True)
        coverage_report = subprocess.check_output("coverage report", shell=True)
        model_coverage = extract_coverage_percent(coverage_report, file_path='library_management/models.py')
        view_coverage = extract_coverage_percent(coverage_report, file_path='library_management/views.py')
        self.assertGreaterEqual(model_coverage, 95, msg='\nدرصد پوشش فایل models.py باید بیشتر از ۹۵% باشد.')
        self.assertGreaterEqual(view_coverage, 90, msg='\nدرصد پوشش فایل views.py باید بیشتر از ۹۰% باشد.')