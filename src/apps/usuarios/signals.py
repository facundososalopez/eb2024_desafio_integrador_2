from django.db.models.signals import post_init, post_save, post_delete
from django.dispatch import receiver
from .models import Usuario

@receiver(post_init, sender=Usuario)
def post_init_usuario(sender, instance, **kwargs):
    instance.__original_avatar = instance.avatar

@receiver(post_save, sender=Usuario)
def post_save_usuario(sender, instance, **kwargs):
    if instance.avatar != instance.__original_avatar and instance.__original_avatar is not None:
        instance.__original_avatar.delete(save=False)

@receiver(post_delete, sender=Usuario)
def post_delete_usuario(sender, instance, **kwargs):
    if instance.avatar != instance.__original_avatar and instance.__original_avatar is not None:
        instance.__original_avatar.delete(save=False)