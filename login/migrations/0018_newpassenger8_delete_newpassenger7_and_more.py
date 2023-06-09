# Generated by Django 4.1 on 2023-01-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_alter_newpassenger7_salutation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newpassenger8',
            fields=[
                ('salutation', models.CharField(blank=True, max_length=10, null=True)),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('passport_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('pass_number', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('pass_email', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Newpassenger8',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Newpassenger7',
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'managed': True},
        ),
    ]
