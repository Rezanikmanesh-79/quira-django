from django.db import migrations, models





class Migration(migrations.Migration):



    dependencies = [

        ('people', '0001_initial'),

    ]



    operations = [

        migrations.AddField(

            model_name='person',

            name='birth_year',

            field=models.PositiveSmallIntegerField(null=True),

        ),

        migrations.AddField(

            model_name='person',

            name='born_in',

            field=models.CharField(max_length=30, null=True),

        ),

        migrations.AddField(

            model_name='person',

            name='first_name',

            field=models.CharField(max_length=30, null=True),

        ),

        migrations.AddField(

            model_name='person',

            name='id_code',

            field=models.CharField(max_length=10, null=True),

        ),

        migrations.AddField(

            model_name='person',

            name='last_name',

            field=models.CharField(max_length=50, null=True),

        ),

    ]