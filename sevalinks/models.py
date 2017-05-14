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
    #user_identifier = models.UUIDField(default=uuid.uuid4, editable=False)
    
    def update_last_login(self):
        self.last_login = timezone.now()
        self.save()
        
    def update_username(self, name):
        self.user_name = name
        self.save()
        
    def update_password(self, password):
        self.password = password
        self.save()

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

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=50)
    service_category = models.CharField(max_length=50)
    
class UserService(models.Model):
    user_service_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    service_title = models.CharField(max_length=50)
    service_Description = models.TextField()
    service_contact = models.IntegerField()
    service_country = models.CharField(max_length=50)
    service_state = models.CharField(max_length=50)
    service_district = models.CharField(max_length=50)
    service_city = models.CharField(max_length=50)
    service_area = models.CharField(max_length=50)
    service_postcode = models.CharField(max_length=10)
    service_created = models.DateTimeField(auto_now=True)
    service_stopped = models.DateTimeField()
    service_active = models.BooleanField()
    service_location_latitude = models.DecimalField(max_digits=12,decimal_places=8)
    service_location_logitude = models.DecimalField(max_digits=12,decimal_places=8)

class ServicePlan(models.Model):
    service_plan_id = models.AutoField(primary_key=True)
    service_plan_name = models.CharField(max_length=50)
    service_plan_description = models.CharField(max_length=50)
    
class UserPlan(models.Model):
    user_plan_id = models.AutoField(primary_key=True)
    user_plan_name = models.CharField(max_length=50)
    user_plan_description = models.CharField(max_length=50)

class PremiumUserPlan(models.Model):    
    user_id = models.ForeignKey(User)
    user_plan_id = models.ForeignKey(UserPlan)
    user_plan_created = models.DateTimeField(auto_now=True)
    user_plan_stopped = models.DateTimeField()
    user_plan_active = models.BooleanField()

class PremiumUserServicePlan(models.Model):    
    user_id = models.ForeignKey(User)
    user_service_id = models.ForeignKey(UserService)
    service_plan_id = models.ForeignKey(ServicePlan)
    service_plan_created = models.DateTimeField(auto_now=True)
    service_plan_stopped = models.DateTimeField()
    service_plan_active = models.BooleanField()
    
class UserContacts(models.Model):
    user_id = models.ForeignKey(User)
    user_contact_id = models.CharField(max_length=50)
    user_contact_created = models.DateTimeField(auto_now=True)
    
class ServiceContacts(models.Model):
    user_id = models.ForeignKey(User)
    service_contact_id = models.ForeignKey(UserService)
    service_contact_created = models.DateTimeField(auto_now=True)
    
    