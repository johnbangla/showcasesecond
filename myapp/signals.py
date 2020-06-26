from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

# pre_save method signal
@receiver(signals.post_save, sender=User)
def check_UserProfile_description(sender,created, instance, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
       
        print("Signal is working") 
# post_save.connect(check_UserProfile_description, sender=UserProfile)
    # if not instance.description:
    #     instance.description = 'This is Default Description'
    
# post_save method
# @receiver(signals.post_save, sender=UserProfile) 
# def create_UserProfile(sender, instance, created, **kwargs):
#     print("Save method is called") 







# def userprofile_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         userprofile = UserProfile.objects.create(user=instance)

#post_save.connect(create_UserProfile, sender=settings.AUTH_USER_MODEL)
