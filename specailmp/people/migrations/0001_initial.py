import json

from django.conf import settings
from django.db import migrations, models


def insert_bad_data(apps, _):
    Person = apps.get_model('people', 'Person')
    with open(settings.BASE_DIR / 'people/fixtures/people.json', 'r') as f:
        people = json.load(f)
    for person in people:
        Person.objects.create(
            fullname=person['fields']['fullname'],
            information=person['fields']['information']
        )


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250, null=True)),
                ('information', models.CharField(max_length=350, null=True)),
            ],
        ),
        migrations.RunPython(
            code=insert_bad_data,
            reverse_code=migrations.RunPython.noop
        )
    ]
