# Generated by Django 5.0 on 2024-03-04 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_restaurant_capasity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='capasity',
            new_name='capacity',
        ),
    ]
