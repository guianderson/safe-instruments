# Generated by Django 4.2.10 on 2024-10-22 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_instrument', '0002_appinstrument_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='appinstrument',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Localização'),
        ),
    ]