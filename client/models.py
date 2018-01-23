from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .validators.image_dimensions import ImageDimensions


class Profile(models.Model):
    """ Класс модели профиля пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField("Дата рождения", null=True)
    avatar = models.ImageField("Аватар", upload_to="client/",
                               null=True, blank=True,validators = [ImageDimensions(200,200)])

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили ползователей"

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, id=instance.id)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
