# Generated by Django 2.0.2 on 2019-06-19 11:36

import complaint.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0008_remove_complaint_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='token',
            field=models.CharField(default=complaint.models.Complaint.token, max_length=255),
        ),
    ]
