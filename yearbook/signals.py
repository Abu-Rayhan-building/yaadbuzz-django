from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import Profile


@receiver(post_save, sender=get_user_model())
def handle_user_register(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
