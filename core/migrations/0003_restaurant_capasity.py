# Generated by Django 5.0 on 2024-03-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_sale_expenditure'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='capasity',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]