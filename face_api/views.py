from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status

from face_api import models

from face_api import FaceRecognition as fr

from face_api.serializers import ImageUploadSerializer

class FaceApi(APIView):
	"""Face uploading and detection api"""
	parser_class=(FileUploadParser,)
	def post(self,request):
		file_serializer=ImageUploadSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save();
			
			unknown_image=file_serializer.data["image"]
			email=file_serializer.data["email"]
			known_person=models.KnowledgeDatabase.objects.get(email=email)
			res={"person":known_person.name ,"status":"unknwon entity"}
			print(known_person.name)
			ret=fr.recognize(str(known_person.image),str(unknown_image))
			print(ret)
			if ret:
				res={"person":known_person.name ,"status":"knwon entity"}
					
				
			

			return Response(res, status=status.HTTP_201_CREATED)


			
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
