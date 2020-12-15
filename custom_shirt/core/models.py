from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager 

 
class UserManager(BaseUserManager):
	
	def create_user(self, email, password=None, **extra_fields):
		"""Create and save a new user"""
		if not email:
			raise ValueError("users most have an email address")

		user = self.model(email=self.normalize_email(email), **extra_fields)
		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, password):
		"""Create a superuser"""
		user = self.create_user(email, password)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)

		return user



class User(AbstractBaseUser):
	"""Custom user model that suppors using email instead of username"""
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'

	objects = UserManager()

	def has_perm(self, perm, obj=None):
		return self.is_superuser

	def has_module_perms(self, app_label):
		return self.is_superuser

