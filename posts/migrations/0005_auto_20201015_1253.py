# Generated by Django 3.0.7 on 2020-10-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20201015_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='post',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
