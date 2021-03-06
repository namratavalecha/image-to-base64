from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
import base64
import time
import hashlib
import json
from Crypto.Cipher import AES
import requests

# Create your views here.

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@api_view(['POST'])
def image_processing(request):
	if 'file_input' not in request.data:
		return Response({'status':status.HTTP_404_NOT_FOUND, 'message':'No file input'})
	
	file = request.data['file_input']

	if file == '':
		return Response({'status':status.HTTP_404_NOT_FOUND, 'message':'Empty file input'})
	
	if file and allowed_file(file.name):
		base64_encode = base64.b64encode(file.read()).decode('utf-8')
		md5_hash = hashlib.md5(base64_encode.encode('utf-8')).hexdigest()
		current_time = int(time.time())
		timestamp = str(current_time)
		key = bytes.fromhex(md5_hash)
		IV = bytes.fromhex(16 * '00')
		aes = AES.new(key, AES.MODE_CBC, IV)
		BS = 16
		pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
		aes_encryption = aes.encrypt(pad(timestamp).encode("utf-8"))
		result = {'md5_hash': str(md5_hash), 'aes_encryption': str(aes_encryption), 'base64_encode': str(base64_encode)}
		return Response({'status':status.HTTP_204_NO_CONTENT, 'message':'File received', 'result': result})
	
	else:
	
		return Response({'status':status.HTTP_404_NOT_FOUND, 'message':'Invalid file name'})



def form_view(request):
	if request.method == 'POST':
		file = request.FILES['file']
		files_dict = {'file_input': file, 'Content-Type': 'image/jpeg'}
		r = requests.post("http://127.0.0.1:8000/core_api/", files = files_dict)
		base64_encode = r.json().get('result').get('base64_encode')
		md5_hash = r.json().get('result').get('md5_hash')
		aes_encryption = r.json().get('result').get('aes_encryption')
		mime = "image/jpg;"
		out_image = f"data:{mime}base64,{base64_encode}"
		return render(request, 'result.html', {'base64_encode' : base64_encode, 'md5_hash' : md5_hash, 'aes_encryption' : aes_encryption, 'out_image' : out_image})
	else:
		return render(request, 'image.html')
