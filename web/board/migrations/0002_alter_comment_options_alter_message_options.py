# Generated by Django 4.1.4 on 2023-01-01 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'managed': False},
        ),
    ]
