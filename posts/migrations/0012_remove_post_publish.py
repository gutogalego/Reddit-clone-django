# Generated by Django 3.0.7 on 2020-10-22 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20201022_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publish',
        ),
    ]
