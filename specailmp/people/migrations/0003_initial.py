from django.db import migrations, models

def info(apps, schema_editor):
    Person = apps.get_model('people', 'Person')

    for person in Person.objects.all():
        try:
            obj = {}
            for x in person.information.split(';') + person.fullname.split(';'):
                s = x.split(':')
                if len(s) == 2:  # اطمینان از اینکه مقدار درست استخراج شده
                    obj[s[0].strip()] = s[1].strip()

            person.id_code = obj.get('id_code', '')  # مقدار پیش‌فرض خالی برای جلوگیری از خطا
            person.born_in = obj.get('born_in', '')

            # بررسی مقدار birth_year قبل از تبدیل به int
            if obj.get('birth_year') and obj['birth_year'].isdigit():
                person.birth_year = int(obj['birth_year'])
            else:
                person.birth_year = None  # مقدار NULL قرار می‌دهیم

            person.first_name = obj.get('first_name', '')
            person.last_name = obj.get('last_name', '')

            person.save()
        except Exception as e:
            print(f'An Error occurred: {e}', person.information.split(';') + person.fullname.split(';'))

class Migration(migrations.Migration):
    dependencies = [
        ('people', '0002_initial'),
    ]

    operations = [
        migrations.RunPython(
            info,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
