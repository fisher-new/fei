# Generated by Django 2.2.11 on 2020-04-21 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0006_proxytoken'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProxyToken',
        ),
    ]
