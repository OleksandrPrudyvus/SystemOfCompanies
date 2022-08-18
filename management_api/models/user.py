from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    """A model that is a representation of the User table in the database"""

    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    office = models.ForeignKey('Office', on_delete=models.SET_NULL, null=True, blank=True)
    repeat_password = models.CharField("repeat_password", max_length=128)
    is_company_admin_user = models.BooleanField(
        verbose_name="company admin status",
        default=False,
        help_text='Determines whether this user is a company administrator'
    )
    is_worker = models.BooleanField(
        verbose_name='company worker status',
        default=False,
        help_text='Determines whether this user is a company worker'
    )

    def get_absolute_url(self):
        return reverse('worker_id', kwargs={'id': self.pk})


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """A signal function that creates a new Token obj for a registered User instance"""
    if created:
        Token.objects.create(user=instance)

