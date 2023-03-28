from django.db import models

# Create your models here.
class Patient(models.Model):

    patient_id = models.IntegerField(null=True)
    patient_name = models.CharField(max_length=100,blank=True)
    dob = models.CharField(max_length=100,blank=True)
    age = models.IntegerField(blank=True)
    phone = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=100,blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.patient_name

class Doctor(models.Model):
    doctor_id = models.IntegerField(null=True)
    doctor_name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=100)
    doctor_details = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.doctor_name

class Appointment(models.Model):
    patient_id = models.IntegerField()
    appointment_id = models.IntegerField(null=True)
    department = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    appointment_data = models.CharField(max_length=100)
    time_slot = models.CharField(max_length=100)
    token_no = models.IntegerField(null=True)
    problem = models.TextField()

    def __str__(self):
        return self.doctor_name

class Room(models.Model):

    room_no = models.IntegerField()
    room_type = models.CharField(max_length=100,null=True)
    patient_name = models.CharField(max_length=100)
    allotment_date = models.CharField(max_length=100)
    discharge_date = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)


    def __str__(self):
        return self.doctor_name


class Patients_Chart(models.Model):

    year = models.IntegerField()
    patients = models.CharField(max_length=100)

    def __int__(self):
        return self.year
    
class Appointment_Chart(models.Model):

    year = models.IntegerField()
    appointments = models.CharField(max_length=100)

    def __int__(self):
        return self.year

class Patient_Payment(models.Model):
    invoice_id = models.IntegerField(default=0)
    invoice_date = models.CharField(max_length=100)
    patient_id = models.IntegerField()
    patient_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    admission_date = models.CharField(max_length=100)
    discharge_date = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100)
    cost_of_treatment = models.IntegerField()
    discount = models.IntegerField()
    advance_paid = models.IntegerField()
    payment_type = models.CharField(max_length=100)
    card_no = models.CharField(max_length=100)
 
    def __str__(self):
        return self.patient_name