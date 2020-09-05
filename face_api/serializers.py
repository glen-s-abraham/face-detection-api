from rest_framework import serializers
from face_api.models import ImageUploads

class ImageUploadSerializer(serializers.ModelSerializer):
	class Meta:
		model=ImageUploads
		fields='__all__'