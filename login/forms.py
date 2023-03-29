from django.forms import ModelForm
from .models import *
from django import forms
from .models import Newpassenger9
from .models import PaymentT



class Contactform(ModelForm):
    class Meta:
        model = Contacttabbb
        fields = ('email', 'cname', 'msg','phone')

        widgets = {
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            'cname' : forms.TextInput(attrs={'class': 'form-control'}),
            'msg' : forms.Textarea(attrs={'class': 'form-control'}),
            'phone' : forms.TextInput(attrs={'class': 'form-control'}),

        }

class Bookingsform(ModelForm):
    class Meta:
        model = BookingsTab
        fields = ('classtype','origin','destination','departure_date','return_date')

        widgets = {
          'classtype': forms.TextInput    (attrs={'placeholder':'Business/Economy','class': 'form-control'}),
            'origin' : forms.TextInput(attrs={'class': 'form-control'}),
            'destination' : forms.TextInput(attrs={'class': 'form-control'}),
            'departure_date' : forms.TextInput(attrs={'placeholder':'yyyy-mm-dd','class': 'form-control'}),
            'return_date' : forms.TextInput(attrs={'placeholder':'yyyy-mm-dd','class': 'form-control'}),
            

        }


class Bookform(ModelForm):
    class Meta:
        model = Newpassenger9
        fields = ('salutation','f_name','l_name','phone','passport_no','pass_email', 'pass_number')

        widgets = {
            'salutation' : forms.TextInput(attrs={'placeholder':'Mr/Mrs,Miss','class': 'form-control'}),
            'f_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'l_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'phone' : forms.TextInput(attrs={'placeholder':'number format: xxxxxxx','class': 'form-control'}),
            'passport_no' : forms.TextInput(attrs={'class': 'form-control'}),
            'pass_email' : forms.TextInput(attrs={'class': 'form-control'}),
            'pass_number' : forms.TextInput(attrs={'class': 'form-control'}),

        }


class Payform(ModelForm):
    class Meta:
        model = PaymentT
        fields = ('card_number','expiry','cvc')

        widgets = {
            'card_number' : forms.TextInput(attrs={'class': 'form-control'}),
            'expiry' : forms.TextInput(attrs={'class': 'form-control'}),
            'cvc' : forms.TextInput(attrs={'class': 'form-control'}),
            
        }









