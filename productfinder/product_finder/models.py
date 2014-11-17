from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=128)
	name = models.CharField(max_length=256)
	phone = models.CharField(max_length=15)
	city = models.CharField(max_length=128)
	country = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.username
		
class Category(models.Model):
	type = models.CharField(max_length=128)
	def __unicode__(self):
		return self.type
	class Meta:
		verbose_name_plural = "Categories"	
class Request(models.Model):
	requester = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	product_name = models.CharField(max_length=256)
	product_brand = models.CharField (max_length=256)
	product_quantity = models.IntegerField(default=1)
	area_local = models.BooleanField(default=True)
	area_online = models.BooleanField(default=True)
	completed = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.product_name

class Response(models.Model):
	text = models.CharField(max_length=800)
	helpful = models.BooleanField(default=False)
	request = models.ForeignKey(Request)
	
	def __unicode__(self):
		return self.text