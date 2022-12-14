# Generated by Django 3.2 on 2022-09-12 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_acquirementsdetail_boughtat'),
    ]

    operations = [
        migrations.AddField(
            model_name='acquirementsdetail',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('ARS', 'ARS')], default='USD', max_length=3, null=True),
        ),
        migrations.RemoveField(
            model_name='acquirementsdetail',
            name='product',
        ),
        migrations.AddField(
            model_name='acquirementsdetail',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product'),
        ),
    ]
