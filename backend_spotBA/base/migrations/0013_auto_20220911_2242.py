# Generated by Django 3.2 on 2022-09-12 01:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20220911_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(blank=True, choices=[('DS', 'DS'), ('VNDS', 'VNDS'), ('USED', 'USED')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='acquirementsdetail',
            name='currency',
            field=models.CharField(blank=True, choices=[('USD', 'USD'), ('ARS', 'ARS')], default='USD', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='provider',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.address'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.phone'),
        ),
    ]
