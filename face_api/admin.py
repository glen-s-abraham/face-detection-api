from django.contrib import admin
from face_api.models import KnowledgeDatabase
from face_api.models import ImageUploads

# Register your models here.
admin.site.register(KnowledgeDatabase)
admin.site.register(ImageUploads)

