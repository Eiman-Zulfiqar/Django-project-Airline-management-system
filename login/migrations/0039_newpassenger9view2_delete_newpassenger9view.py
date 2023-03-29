# Generated by Django 4.1 on 2023-01-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0038_newpassenger9view'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newpassenger9View2',
            fields=[
                ('f_name', models.CharField(max_length=20)),
                ('passport_no', models.CharField(max_length=10)),
                ('pass_number', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'NEWPASSENGER9_VIEW2',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Newpassenger9View',
        ),
    ]
