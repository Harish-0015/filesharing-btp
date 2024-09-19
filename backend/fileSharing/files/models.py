from django.db import models
from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import AbstractUser
import random

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    unique_id = models.CharField(max_length=8)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def profile(self):
        profile = Profile.objects.get(user=self)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    bio = models.CharField(max_length=100)
    image = models.ImageField(upload_to="user_images", default="default.jpg")
    verified = models.BooleanField(default=False)



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def generate_unique_id():
    unique_id = str(random.randint(10000000, 99999999))  # Generate 8-digit number
    while User.objects.filter(unique_id=unique_id).exists():  # Check for uniqueness
        unique_id = str(random.randint(10000000, 99999999))  # Generate again if exists
    return unique_id
        
def pre_save_user_receiver(sender, instance, *args, **kwargs):
    if not instance.unique_id:  # If no unique_id assigned yet
        instance.unique_id = generate_unique_id()

pre_save.connect(pre_save_user_receiver,sender=User)
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)