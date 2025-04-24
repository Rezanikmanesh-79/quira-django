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


def run_tests():
    result = subprocess.run("python3 manage.py test library_management", shell=True)
    return result


class TestAll(TestCase):
    PASSED = (0,)
    MODELS_PATH = "library_management/models.py"
    TESTS_PATH = "library_management/tests.py"

    @copy_content("library_management/temp_tests_file.py", TESTS_PATH)
    def setUp(self):
        empty_file(self.MODELS_PATH)

    def tearDown(self):
        empty_file(self.TESTS_PATH)

    @copy_content("tests/sample1.txt", MODELS_PATH)
    def test_correct_answer(self):
        result = run_tests()
        self.the_tests_should_pass(result)

    @copy_content("tests/sample2.txt", MODELS_PATH)
    def test_none_result(self):
        result = run_tests()
        self.the_tests_should_fail(result)

    def the_tests_should_fail(self, result):
        self.assertNotIn(result.returncode, self.PASSED, msg="\nتست‌هایی که نوشته‌اید، برای یک کد غلط، پاس می‌شوند؛ در حالی که نباید پاس شوند.")

    def the_tests_should_pass(self, result):
        self.assertIn(result.returncode, self.PASSED, msg="\nتست‌هایی که نوشته‌اید، برای یک کد صحیح، پاس نمی‌شوند؛ در حالی که باید پاس شوند.")