# Generated by Django 5.0.6 on 2024-07-18 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
