# Generated by Django 4.1 on 2023-01-07 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_contact_delete_contactustab_alter_tickettab_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacttab',
            fields=[
                ('sno', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('cname', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('ccontent', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'ContactTab',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='tickettab',
            name='flight_no',
            field=models.ForeignKey(blank=True, db_column='flight_no', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login.newflightavailable'),
        ),
        migrations.AddField(
            model_name='tickettab',
            name='passport_no',
            field=models.ForeignKey(blank=True, db_column='passport_no', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login.newpassenger4'),
        ),
    ]
