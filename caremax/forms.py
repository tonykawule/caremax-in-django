
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields ='__all__'

class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'  

class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__'      

class BillForm(ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ['item_name', 'stockcategory', 'quantity']       

 
class StockcategoryForm(ModelForm):
    class Meta:
        model = Stockcategory
        fields = '__all__'    


class IssueForm(ModelForm):
    class Meta:
        model = Stock
        fields = ['issued_quantity', 'issued_to']

class ReceiveForm(ModelForm):
    class Meta:
        model = Stock
        fields = ['quantity_received', 'received_by']

class ReorderLevelForm(ModelForm):
    class Meta:
        model = Stock
        fields = ['reorder_level']                