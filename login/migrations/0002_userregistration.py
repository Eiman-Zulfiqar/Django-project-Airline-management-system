# Generated by Django 4.1 on 2023-01-05 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userregistration',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password1', models.CharField(max_length=8)),
                ('password2', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'UserRegistration',
                'managed': False,
            },
        ),
    ]