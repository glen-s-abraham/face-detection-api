from django.db import models
from datetime import date

class KnowledgeDatabase(models.Model):
	"""Update and store images to comapre uploaded ones"""
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=100)
	image=models.FileField(upload_to='known_images')

	def __str__(self):
		return self.name

class ImageUploads(models.Model):
	"""To hold teh uploaded images"""
	email=models.EmailField(max_length=100)
	image=models.FileField(upload_to='uploaded_images')
	timestamp=models.DateField(default=date.today)
	def __str__(self):
		return self.timestamp