# Generated by Django 2.1.3 on 2018-12-05 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='password',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='username',
        ),
    ]
