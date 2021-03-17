from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *


class ComputeView(APIView):

    serializer_class = ComputeSerializer
    
    def get(self, request, format=None):
             
        output = [{"number": output.number, "serie_fibonacci": output.serie_fibonacci}
                  for output in Compute.objects.all()]
        return Response(output)
    
    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
        
            res = serializer.validated_data.get('number')
            res = int(res)
            if res <= 0:
                return HttpResponseBadRequest("Please enter a positive integer number")
            else:
                result = [fibonacci(i) for i in range(res)]

            serializer.validated_data['serie_fibonacci'] = result            

            serializer.save()                        
            return Response(result)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
                
                

