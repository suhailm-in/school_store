# Generated by Django 4.2.2 on 2023-06-23 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_alter_person_address_alter_person_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
