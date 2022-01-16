from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete = models.SET_NULL, null=True )
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL ,null=True)#IF WE BRING TOPIC DOWN WRAP TOPIC IN A STRING "TOPIC"
    name = models.CharField(max_length=200)
    description = models.TextField(null = True , blank=True)
    participants = models.ManyToManyField(User , related_name="participants" , blank = True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #SET_NULL to save the messages of the room\
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(blank=True , null=True) 


    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
