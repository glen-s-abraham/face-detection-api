import face_recognition
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def recognize(known_file,unknown_file):
	"""Face recognizer"""

	#define full path
	
	known_path=os.path.join(BASE_DIR,'media',known_file)

	unknown_path=str(BASE_DIR)+str(unknown_file)
	
	
	if os.path.exists(known_path) and os.path.exists(unknown_path):
	
	
		#generate encoding for the known faces
		known_image=face_recognition.load_image_file(known_path)
		knwon_encodings=face_recognition.face_encodings(known_image)[0]

		#generate encoding for the unknown faces
		unknown_image=face_recognition.load_image_file(unknown_path)
		unknwon_encodings=face_recognition.face_encodings(unknown_image)[0]

		#compare the two encodings
		result=face_recognition.compare_faces([knwon_encodings],unknwon_encodings)
		
		return result[0]
	else:
		return False	

print(recognize('obama.jpg','test.jpg'))