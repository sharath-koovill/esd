from django import forms
import configs

class UserRegisterForm(forms.Form):
    first_name = forms.CharField(label="First name",max_length=50, required=True)
    last_name = forms.CharField(label="Last name",max_length=50, required=True)
    username = forms.CharField(label="Username",max_length=50, required=True)
    email = forms.EmailField(label="Email", required=True)
    confirm_email = forms.EmailField(label="Confirm email", required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)
    phone_number = forms.IntegerField(label="Mobile number", required=True)
    cb = forms.CharField()
    
class UserLoginForm(forms.Form):    
    email = forms.EmailField(label="Email address", required=True)    
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)
    
class ImageUploadForm(forms.Form):
    """Image upload form."""
    user_image = forms.ImageField()
    
class UserLocationForm(forms.Form):
    user_country = forms.CharField(max_length=50, required=True)
    user_state = forms.CharField(max_length=50, required=True, widget=forms.Select(choices=configs.STATES))
    user_area = forms.CharField(max_length=50, required=True)
    user_postcode = forms.CharField(max_length=10, required=True)
    
class UserStateForm(forms.Form):   
    user_state = forms.CharField(label="State", max_length=50, required=True, widget=forms.Select(choices=configs.STATES))
    
class UserProfessionForm(forms.Form):
    user_job_designation = forms.CharField(max_length=50, widget=forms.Select(choices=configs.DESIGNATION))
    user_experience = forms.CharField(max_length=50, required=True, widget=forms.Select(choices=configs.EXPERIENCE))
    user_industry = forms.CharField(max_length=50, widget=forms.Select(choices=configs.INDUSTRY))
    user_company = forms.CharField(max_length=50)
    user_profession = forms.CharField(max_length=50, required=True)
    user_description = forms.CharField()    
    