# Generated by Django 4.1 on 2023-01-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0037_oldpricetab_delete_oldprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newpassenger9View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(db_collation='USING_NLS_COMP', max_length=20)),
                ('passport_no', models.CharField(db_collation='USING_NLS_COMP', max_length=10)),
            ],
            options={
                'db_table': 'NEWPASSENGER9_VIEW',
                'managed': False,
            },
        ),
    ]