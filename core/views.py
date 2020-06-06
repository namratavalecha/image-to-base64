from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def image_processing(request):
	print(request.POST)
	if 'file_input' not in request.data:
		return Response({'status':status.HTTP_404_NOT_FOUND, 'message':'Invalid! Input a file.'})
	file = request.POST.get('file_input')
	print(file.stream.read())
	return Response({'status':status.HTTP_204_NO_CONTENT, 'message':'File received'})


