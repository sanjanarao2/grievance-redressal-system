# Generated by Django 2.0.2 on 2019-06-10 06:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('contact', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(default='123@xyz.org', max_length=254)),
                ('complaint', models.CharField(max_length=1000)),
            ],
        ),
    ]
