from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import configs
import uuid

# Create your models here.
class User(models.Model):    
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    user_created = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    user_active = models.BooleanField(default=False)
    user_type = models.CharField(max_length=2, default='PR', choices=configs.USER_TYPE)
    user_identifier = models.UUIDField(default=uuid.uuid4, editable=False)
       
class UserConfirmation(models.Model):
    user_id = models.ForeignKey(User)
    user_confirmation_id = models.CharField(max_length=100)
    user_confirmed = models.BooleanField(default=False)
    confirmation_completed = models.DateTimeField(null=True)

class UserLocation(models.Model):
    user_id = models.ForeignKey(User)
    user_country = models.CharField(max_length=50)
    user_state = models.CharField(max_length=50, choices=configs.STATES)
    user_district = models.CharField(default="", max_length=50)
    user_city = models.CharField(default="", max_length=50)
    user_area = models.CharField(max_length=50)
    user_postcode = models.CharField(max_length=10)
    user_location_latitude = models.DecimalField(null=True, max_digits=12,decimal_places=8)
    user_location_logitude = models.DecimalField(null=True, max_digits=12,decimal_places=8)
    
class UserProfession(models.Model):
    user_id = models.ForeignKey(User)
    user_job_designation = models.CharField(max_length=50, null=True, choices=configs.DESIGNATION)
    user_experience = models.CharField(max_length=50, choices=configs.EXPERIENCE)
    user_industry = models.CharField(max_length=4, null=True, choices=configs.INDUSTRY)
    user_profession = models.CharField(max_length=50)
    user_company = models.CharField(null=True, max_length=50)
    user_description = models.TextField(null=True)
    
class UserEducation(models.Model):
    user_id = models.ForeignKey(User)
    user_college = models.CharField(max_length=50)
    user_college_start = models.DateField()
    user_college_end = models.DateField()
    user_college_active = models.BooleanField(default=True)
    user_Description = models.TextField()

class UserResetPassword(models.Model):
    user_id = models.ForeignKey(User)
    reset_id = models.CharField(max_length=100)
    password_reset = models.BooleanField(default=False)
    reset_request = models.DateTimeField(auto_now=True)
    reset_completed = models.DateTimeField(null=True)

class UserImage(models.Model):
    user_id = models.ForeignKey(User)
    user_image = models.ImageField()

class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    subscription_name = models.CharField(max_length=50)
    subscription_description = models.CharField(max_length=50)
    
class UserSubscription(models.Model):    
    user_id = models.ForeignKey(User)
    user_subscription_id = models.ForeignKey(Subscription)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(null=True)
    user_subscription_active = models.BooleanField(default=True)   


    
    