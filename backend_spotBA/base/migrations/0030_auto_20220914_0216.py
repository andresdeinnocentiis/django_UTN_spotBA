# Generated by Django 3.2 on 2022-09-14 05:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_alter_product_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='acquirementsdetail',
            name='soldAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acquirementsdetail',
            name='soldPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
