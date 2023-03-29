# Generated by Django 4.1 on 2023-01-14 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0023_newflightavailable_businessclass_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newflightavailable',
            name='Businessclass',
        ),
        migrations.AlterField(
            model_name='bookingstab',
            name='classtype',
            field=models.CharField(default='economy', max_length=10),
        ),
        migrations.AlterField(
            model_name='bookingstab',
            name='origin',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='newpassenger9',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss')], default='Mr', max_length=10, null=True),
        ),
    ]
