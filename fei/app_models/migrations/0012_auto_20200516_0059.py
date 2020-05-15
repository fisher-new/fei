# Generated by Django 2.2.11 on 2020-05-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0011_anonymouscomments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anonymouscomments',
            old_name='username',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='anonymouscomments',
            name='comments',
            field=models.TextField(max_length=200),
        ),
    ]
