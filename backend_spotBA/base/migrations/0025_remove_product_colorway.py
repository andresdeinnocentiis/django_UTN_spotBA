# Generated by Django 3.2 on 2022-09-14 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_auto_20220913_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colorway',
        ),
    ]
