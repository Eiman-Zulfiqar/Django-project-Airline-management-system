# Generated by Django 4.1 on 2023-01-07 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_alter_newpassenger7_f_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpassenger7',
            name='salutation',
            field=models.CharField(blank=True, default='Mr', max_length=10),
        ),
    ]