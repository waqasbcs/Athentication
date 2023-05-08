from django.contrib.auth.models import User
from  django  import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class signupform(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput)  
    class Meta:
        model=User
        fields=('username','first_name','last_name','email')
        labels={'email':'Email'}
        
class edituserprofileform(UserChangeForm):
    password = None
    class Meta:
      model=User
      fields=['username','first_name', 'last_name','email','date_joined','last_login','is_active']
      labels={'email':'Email'}
        