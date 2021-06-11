from django.db.models.signals import post_save

# and User model is going to be sender means it send the signal which is catch by post_save
from django.contrib.auth.models import User

# this is receiver
from django.dispatch import receiver

# and we were creating profile in our model so we need profile
from .models import Profile

# 1.when new user is created/saved then it send a singnal of post_save because post_save fired when any object is saved
# 2.the function create_profile have a decorator::  @receiver(singnal_type, sender) which receive signal if sender send perticular signal here signal_type = post_save and sender is User
# 3.when create_profile receive signal then post_save passed parameter of that signal to function:
#     a)sender: who send the signal
#     b)instance: the instance of sender means (object of User)
#     c)created: bool value that user created or not
#     d)**kwargs: some argument
# 4.if user is created then make a Profile object and add assign profile object to that user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# when usr is aggign to profile object then save the profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    instance.profile.save()

