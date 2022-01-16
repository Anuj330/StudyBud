# this form is to modify the django form 

from django.forms import ModelForm
from .models import Room, Message
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields ='__all__'
        
        excludes = 'participants', 'host'
        
class UserForm(ModelForm):
    class Meta:
        model = Message
        fields = ['user', 'profile_pic']
