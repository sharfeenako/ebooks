# Generated by Django 3.2.12 on 2023-05-20 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_book_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='original_price',
            new_name='price',
        ),
    ]
