from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status

from face_api.serializers import ImageUploadSerializer

class FaceApi(APIView):
	"""Face uploading and detection api"""
	parser_class=(FileUploadParser,)
	def post(self,request):
		file_serializer=ImageUploadSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save();
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
