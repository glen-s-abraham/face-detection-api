from face_api.views import FaceApi
from django.urls import path,include

urlpatterns = [
    path('',FaceApi.as_view())

]