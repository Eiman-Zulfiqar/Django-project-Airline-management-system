# Generated by Django 4.1 on 2023-01-17 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0042_alter_bookingstab_classtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpassenger9',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], default='Mr', max_length=10, null=True),
        ),
    ]