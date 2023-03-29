from django.db import models



# Create your models here.

class Newpassenger9(models.Model):
    Status = (
        ('Mr','Mr'),('Mrs','Mrs'),('Ms','Ms')
    )
    salutation = models.CharField(max_length=10, blank=True, null=True, choices=Status, default='Mr')
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    passport_no = models.CharField(max_length=10, blank=False, null=False, default='00000')
    pass_number = models.BigAutoField(primary_key=True)
    pass_email = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'Newpassenger9'


class Newpassenger9View2(models.Model):
    f_name = models.CharField(max_length=20)
    passport_no = models.CharField(max_length=10)
    pass_number = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'NEWPASSENGER9_VIEW2'

class Employeeblock(models.Model):
    ssid = models.BigIntegerField(primary_key=True)
    emp_dob = models.CharField(max_length=10, blank=True, null=True)
    emp_phone = models.BigIntegerField(blank=True, null=True)
    emp_email = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'EMPLOYEEBLOCK'


class Databackup(models.Model):
    ssid = models.BigIntegerField(primary_key=True)
    emp_dob = models.CharField(max_length=10, blank=True, null=True)
    emp_phone = models.BigIntegerField(blank=True, null=True)
    emp_email = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'DATABACKUP'




class Tticket(models.Model):
    pnr_no = models.BigIntegerField(unique=True, blank=True, null=True)
    f_source = models.CharField(max_length=10, blank=True, null=True)
    f_destination = models.CharField(max_length=10, blank=True, null=True)
    seat_no = models.BigAutoField(primary_key=True)
    no_of_tickets = models.BigIntegerField(blank=True, null=True)
    pass_number = models.ForeignKey('Newpassenger9', models.DO_NOTHING, db_column='pass_number', blank=True, null=True)
    flight_no = models.ForeignKey('NewFlightAvailable', models.DO_NOTHING, db_column='flight_no', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TTicket'




class Contacttabbb(models.Model):
    sno = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=20)
    cname = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    msg = models.CharField(max_length=250)

    class Meta:
        managed = True
        db_table = 'Contacttabbb'


class PaymentT(models.Model):
    card_number = models.BigIntegerField(primary_key=True)
    expiry = models.DateField()
    cvc = models.BigIntegerField()
    bookng_no = models.ForeignKey('BookingsTab', models.DO_NOTHING, db_column='bookng_no', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Payment_T'


class BookingsTab(models.Model):

    Status = (
        ('Business','Business'),('economy','economy'),('Economy','Economy'),('business','business')
    )
    bookng_no = models.BigAutoField(primary_key=True)
    classtype = models.CharField(max_length=10, blank=False, null=False, choices= Status, default='Economy')     
    origin = models.CharField(max_length=10, blank=True, null=True)        
    destination = models.CharField(max_length=10, blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    flight_no = models.ForeignKey('NewFlightAvailable', models.DO_NOTHING, 
   
    db_column='flight_no', blank=True, null=True )

    class Meta:
        managed = True
        db_table = 'BOOKINGS_TAB'


class NewFlightAvailable(models.Model):
    airbus_no = models.CharField(max_length=10, blank=True, null=True)     
    flight_no = models.BigAutoField(primary_key=True)
    origin = models.CharField(max_length=10, blank=True, null=True)        
    destination = models.CharField(max_length=10, blank=True, null=True)   
    departure_date = models.DateField(blank=True, null=True)
    departure_time = models.DateTimeField(blank=True, null=True)
    journey_hours = models.BigIntegerField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    No_of_seats = models.BigIntegerField(blank=True, null=True)
    Msg = models.CharField(max_length=30, null=True)

    class Meta:
        managed = True
        db_table = 'NEW_FLIGHT_AVAILABLE'

class NewFlightAvailableView(models.Model):
    flight_no = models.BigAutoField(primary_key=True)
    origin = models.CharField(max_length=10,  blank=True, null=True)
    destination = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NEW_FLIGHT_AVAILABLE_VIEW'

class OldpriceTab(models.Model):
    flight_no = models.BigIntegerField(primary_key=True)
    airbus_no = models.CharField(max_length=10, blank=True, null=True)
    origin = models.CharField(max_length=20, blank=True, null=True)
    destination = models.CharField(max_length=20, blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'OLDPRICE_TAB'
