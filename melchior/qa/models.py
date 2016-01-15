from __future__ import unicode_literals

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=250)
    abbreviation = models.CharField(max_length=30)


class GenericUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_number, password=None):
      user = self.model(
        email= GenericUserManager.normalize_email(email),
        first_name= first_name.title(),
        last_name= last_name.title(),
        phone_number = phone_number,
        is_active = True
      )
      user.set_password(password)
      user.save()

      return user

    def create_superuser(self, email, first_name, last_name, phone_number, password):
      user = self.model(
        email= GenericUserManager.normalize_email(email),
        first_name= first_name.title(),
        last_name= last_name.title(),
        phone_number = phone_number,
        is_active = True,
        is_admin = True,
      )
      user.set_password(password)
      user.save()

      return user



class GenericUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True, blank=True)
    is_admin = models.BooleanField(default=False, blank=True)
    phone_number = models.CharField(max_length=10, null=True) 
    organization = models.ForeignKey(Organization, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    objects = GenericUserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_perms(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_active(self):
    #   return self.is_active

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

class InternalUser(GenericUser):
  pass

