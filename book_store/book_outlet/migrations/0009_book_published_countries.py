# Generated by Django 5.0.3 on 2024-03-14 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0008_country_alter_address_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(to='book_outlet.country'),
        ),
    ]
