# Generated by Django 2.0.7 on 2018-08-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20180817_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='poll_logo',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]