from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

	user = models.OneToOneField(User)
	name = models.CharField(max_length=256)
	phone = models.CharField(max_length=15)
	city = models.CharField(max_length=128)
	country = models.CharField(max_length=128)

	def __unicode__(self):
		return self.user.username

class Category(models.Model):
	type = models.CharField(max_length=128)
	icon = models.CharField(max_length=256)
	image = models.CharField(max_length=600)
	def __unicode__(self):
		return self.type
	class Meta:
		verbose_name_plural = "Categories"
		
class Request(models.Model):
	requester = models.ForeignKey(UserProfile)
	category = models.ForeignKey(Category)
	product_name = models.CharField(max_length=256)
	description = models.CharField(max_length=600)
	product_brand = models.CharField (max_length=256)
	product_quantity = models.IntegerField(default=1)
	area_local = models.BooleanField(default=True)
	area_online = models.BooleanField(default=True)
	completed = models.BooleanField(default=False)

	def __unicode__(self):
		return self.product_name
