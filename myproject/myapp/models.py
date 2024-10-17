from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# inherit user built-in model here
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

# Create Signals to Automatically Create/Update Profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Create your models here.
class Msg(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    # sender = models.CharField(max_length=255)
    msg = models.TextField(default='')
    senton = models.DateTimeField(default=datetime.now())  # automatically set to current date and time when the object is created
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_DEFAULT, default=1)
    # user = models.ManyToOneRel(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
