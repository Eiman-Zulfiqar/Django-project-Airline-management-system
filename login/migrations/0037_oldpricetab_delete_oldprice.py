# Generated by Django 4.1 on 2023-01-15 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0036_remove_oldprice_id_oldprice_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='OldpriceTab',
            fields=[
                ('flight_no', models.BigIntegerField(primary_key=True, serialize=False)),
                ('airbus_no', models.CharField(blank=True, max_length=10, null=True)),
                ('origin', models.CharField(blank=True, max_length=20, null=True)),
                ('destination', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'OLDPRICE_TAB',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Oldprice',
        ),
    ]