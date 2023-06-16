from django.db import models


class MenuItem(models.Model):
	name= models.CharField(max_length=100)
	description=models.TextField()
	image = models.ImageField(upload_to='menu_images/')
	price = models.DecimalField(max_digits=5, decimal_places=2)
	category= models.ManyTOManyField('Category', related_name='item')

	def_str_(self):
       return self.name


class Category(models.Model):
	name= models.CharField(max_lenght=100)

	def_str_(self):
	   return self.name 

class OrderModel(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	items = models.ManyTOManyField(
		'MenuItem', related_name='order', blank=True)

	def_str_(self):
	   return f'Order: {self.created_on.strftime("%b %d %I: %M %p')}

