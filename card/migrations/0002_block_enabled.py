# Generated by Django 4.0.4 on 2022-04-16 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
