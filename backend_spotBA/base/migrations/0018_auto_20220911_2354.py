# Generated by Django 3.2 on 2022-09-12 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_acquirementsdetail_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
