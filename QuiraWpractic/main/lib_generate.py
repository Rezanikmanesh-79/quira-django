import os
import django
from faker import Faker
from librarry.models import Library  # Replace 'myapp' with the name of your app

# Set up Django environment if running standalone
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  # Replace 'project' with your project name
django.setup()

# Initialize Faker
faker = Faker()

# Generate 100 fake libraries
def create_fake_libraries(n=100):
    libraries = []
    for _ in range(n):
        libraries.append(Library(number=faker.random_int(min=1, max=1000)))  # Random number for the 'number' field
    
    # Bulk create for performance
    Library.objects.bulk_create(libraries)
    print(f"{n} fake libraries created successfully.")

# Run the script
if __name__ == "__main__":
    create_fake_libraries()
