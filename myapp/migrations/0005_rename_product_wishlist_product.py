# Generated by Django 4.2.3 on 2023-08-01 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='Product',
            new_name='product',
        ),
    ]
