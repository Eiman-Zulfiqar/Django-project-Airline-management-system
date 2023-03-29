# Generated by Django 4.1 on 2023-01-07 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_contacttabbb_delete_contacttabb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newpassenger7',
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
                'db_table': 'NewPassenger7',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('pnr_no', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('f_source', models.CharField(blank=True, max_length=10, null=True)),
                ('f_destination', models.CharField(blank=True, max_length=10, null=True)),
                ('seat_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('no_of_tickets', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Ticket__',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentT',
            fields=[
                ('card_number', models.BigIntegerField(primary_key=True, serialize=False)),
                ('expiry', models.DateField()),
                ('cvc', models.BigIntegerField()),
                ('bookng_no', models.ForeignKey(blank=True, db_column='bookng_no', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login.bookingstab')),
            ],
            options={
                'db_table': 'Payment_T',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='paymenttab',
            name='bookng_no',
        ),
        migrations.RemoveField(
            model_name='tickettab',
            name='flight_no',
        ),
        migrations.RemoveField(
            model_name='tickettab',
            name='passport_no',
        ),
        migrations.DeleteModel(
            name='Newpassenger4',
        ),
        migrations.DeleteModel(
            name='PaymentTab',
        ),
        migrations.DeleteModel(
            name='TicketTab',
        ),
    ]
