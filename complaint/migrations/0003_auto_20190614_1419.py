# Generated by Django 2.0.2 on 2019-06-14 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0002_complaint_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='email',
        ),
    ]
