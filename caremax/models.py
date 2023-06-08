from django.db import models

# Create your models here.

gender_choices = [
    ('Male', 'Male'),
    ('Female', 'Female')
]


class Patient(models.Model):
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null= False)
    contact = models.CharField(max_length=20, null=False)
    allergy = models.CharField(max_length=100, null= True)
    address = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=7, null= True, choices = gender_choices)
    email = models.CharField(max_length=80, null= True)
    nextofkin = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=20, null= True)
    relationship = models.CharField(max_length=7, null= True)


    def __str__(self):
        return self.name

class Visit(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    pastcomplaint = models.CharField(max_length=100, null=True)
    presentcomplaint = models.CharField(max_length=100, null=True)
    recommendation = models.CharField(max_length=100, null = True)
    patient_id = models.ForeignKey(Patient, on_delete= models.CASCADE, related_name='display_visits')

    def __str__(self):
        return self.presentcomplaint

class Test(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True)
    testname = models.CharField(max_length=50, null=True)   
    testresults = models.CharField(max_length=100, null=True)
    patient_id = models.ForeignKey(Patient, on_delete= models.CASCADE, related_name='display_tests') 

    def __str__(self):
        return self.testname

class Treatment(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True)
    treatmentname = models.CharField(max_length=50, null=True)   
    doze = models.TextField(max_length=200, null=True) 
    remarks = models.TextField(max_length=200, null=True)
    patient_id = models.ForeignKey(Patient, on_delete= models.CASCADE, related_name='display_treatments') 

    def __str__(self):
        return self.treatmentname

class Bill(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True)
    bill = models.IntegerField()
    amountpaid = models.IntegerField()
    balance = models.IntegerField()
    patient_id = models.ForeignKey(Patient, on_delete= models.CASCADE, related_name='display_bills')

    def __str__(self):
        return self.amountpaid

  
class Stockcategory(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    item_name = models.CharField(max_length=100)
    stockcategory = models.ForeignKey(Stockcategory, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True)
    rate = models.IntegerField(default=0, null=True)
    quantity_received = models.IntegerField(default=0)
    issued_quantity = models.IntegerField(default=0)
    received_by = models.CharField(max_length=100, null=True)
    issued_by = models.CharField(max_length=100, null=True)
    issued_to = models.CharField(max_length=100, null=True)
    created_by = models.CharField(max_length=100, null=True)
    reorder_level = models.IntegerField(default=0, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True)
    export_to_csv = models.BooleanField(default=True)
    
    def __str__(self):
        return self.item_name    

