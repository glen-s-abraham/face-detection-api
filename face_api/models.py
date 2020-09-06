from django.db import models

class KnowledgeDatabase(models.Model):
	"""Update and store images to comapre uploaded ones"""
	name=models.CharField(max_length=50)
	image=models.FileField(upload_to='/known_images')
	def __str__(self):
		return self.name

class ImageUploads(models.Model):
	"""To hold teh uploaded images"""
	image=models.FileField(upload_to='/uploaded_images')
	def __str__(self):
		return self.image.name