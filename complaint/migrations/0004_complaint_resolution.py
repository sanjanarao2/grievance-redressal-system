# Generated by Django 2.2.1 on 2019-06-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0003_complaint_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='resolution',
            field=models.CharField(default=' ', max_length=1000),
            preserve_default=False,
        ),
    ]
