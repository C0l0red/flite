# Generated by Django 2.2 on 2021-06-06 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210606_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='p2ptransfer',
            old_name='receipient',
            new_name='recipient',
        ),
    ]
