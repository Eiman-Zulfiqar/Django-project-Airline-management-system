# Generated by Django 4.1 on 2023-01-07 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_newflightavailable_msg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('cname', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('ccontent', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'Contact',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='ContactUsTab',
        ),
        migrations.AlterModelOptions(
            name='tickettab',
            options={'managed': True},
        ),
    ]
