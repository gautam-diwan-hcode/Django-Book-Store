# Generated by Django 5.0.3 on 2024-03-13 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='book_outlet.address'),
        ),
    ]
