# Generated by Django 4.1 on 2023-01-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_newflightavailable_no_of_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='newflightavailable',
            name='Msg',
            field=models.CharField(max_length=30, null=True),
        ),
    ]