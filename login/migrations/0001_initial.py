# Generated by Django 4.1 on 2023-01-03 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingsTab',
            fields=[
                ('bookng_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('classtype', models.CharField(blank=True, max_length=10, null=True)),
                ('origin', models.CharField(blank=True, max_length=10, null=True)),
                ('destination', models.CharField(blank=True, max_length=10, null=True)),
                ('departure_date', models.DateField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'BOOKINGS_TAB',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ContactUsTab',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('c_name', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'CONTACT_US_TAB',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employeet',
            fields=[
                ('ssid', models.BigAutoField(primary_key=True, serialize=False)),
                ('emp_dob', models.CharField(blank=True, max_length=10, null=True)),
                ('emp_phone', models.BigIntegerField(blank=True, null=True)),
                ('emp_email', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'EMPLOYEEt',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('email', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('admin_password', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'LOGIN',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NewFlightAvailable',
            fields=[
                ('airbus_no', models.CharField(blank=True, max_length=10, null=True)),
                ('flight_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('origin', models.CharField(blank=True, max_length=10, null=True)),
                ('destination', models.CharField(blank=True, max_length=10, null=True)),
                ('departure_date', models.DateField(blank=True, null=True)),
                ('departure_time', models.DateTimeField(blank=True, null=True)),
                ('journey_hours', models.BigIntegerField(blank=True, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'NEW_FLIGHT_AVAILABLE',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Newpassenger4',
            fields=[
                ('salutation', models.CharField(blank=True, max_length=10, null=True)),
                ('f_name', models.CharField(blank=True, max_length=20, null=True)),
                ('l_name', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('passport_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('pass_number', models.BigIntegerField()),
                ('pass_email', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'NEWPASSENGER4',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ticket3Tab',
            fields=[
                ('pnr_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('f_source', models.CharField(blank=True, max_length=10, null=True)),
                ('f_destination', models.CharField(blank=True, max_length=10, null=True)),
                ('seat_no', models.BigIntegerField(blank=True, null=True)),
                ('no_of_tickets', models.BigIntegerField(blank=True, null=True)),
                ('flight_no', models.ForeignKey(blank=True, db_column='flight_no', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login.newflightavailable')),
                ('passport_no', models.ForeignKey(blank=True, db_column='passport_no', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login.newpassenger4')),
            ],
            options={
                'db_table': 'TICKET3_TAB',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PaymentTab',
            fields=[
                ('card_number', models.BigIntegerField(primary_key=True, serialize=False)),
                ('expiry', models.DateField(blank=True, null=True)),
                ('cvc', models.BigIntegerField(blank=True, null=True)),
                ('bookng_no', models.ForeignKey(blank=True, db_column='bookng_no', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login.bookingstab')),
            ],
            options={
                'db_table': 'PAYMENT_TAB',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='bookingstab',
            name='flight_no',
            field=models.ForeignKey(blank=True, db_column='flight_no', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login.newflightavailable'),
        ),
    ]
