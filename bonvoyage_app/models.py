from django.db import models

# Create your models here.
class userregmodel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class agencyregmodel(models.Model):
    agency=models.CharField(max_length=20)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class uploadmodel(models.Model):
    catchoice = [
        ('food', 'food'),
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    choice = [
        ('pet', 'pet'),
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    choices = [
        ('0-0', '0-0'),
        ('0-1', '0-1'),
        ('1-2', '1-2'),
        ('2-3', '2-3'),
        ('3-4', '3-4'),
        ('4-5', '4-5'),
        ('5-6', '5-6'),
        ('6-7', '6-7'),
        ('7-8', '7-8'),
        ('8-9', '8-9'),
        ('9-10', '9-10'),
    ]
    mychoice = [
        ('cab', 'cab'),
        ('yes', 'yes'),
        ('no', 'no')
    ]
    agency=models.CharField(max_length=30)
    email=models.EmailField()
    state=models.CharField(max_length=30)
    spots=models.CharField(max_length=500)
    food=models.CharField(max_length=30,choices=catchoice)
    pet=models.CharField(max_length=30,choices=choice)
    duration=models.CharField(max_length=30,choices=choices)
    cab=models.CharField(max_length=30,choices=mychoice)
    stay=models.CharField(max_length=30)
    rate=models.CharField(max_length=30)

class bookmodel(models.Model):
    agency=models.CharField(max_length=20)
    state=models.CharField(max_length=300)
    spots=models.CharField(max_length=500)
    rate=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    frmdy=models.CharField(max_length=20)
    tody=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=20)

class wishmodel(models.Model):
    agency = models.CharField(max_length=30)
    email = models.EmailField()
    state = models.CharField(max_length=30)
    spots = models.CharField(max_length=500)
    food = models.CharField(max_length=30)
    pet = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
    cab = models.CharField(max_length=30)
    stay = models.CharField(max_length=30)
    rate = models.CharField(max_length=30)
