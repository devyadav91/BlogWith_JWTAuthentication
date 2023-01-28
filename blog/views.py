from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializer import PersonSerializer
from .models import Person
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserApiView(APIView):

    authentication_classes=[JWTAuthentication]
    serializer_class = PersonSerializer
    permission_classes=[IsAuthenticated]
    http_method_names = ['get','post','put','delete']

    def get(self,request,pk=None, format=None):        
        items=Person.objects.all()
        serializer = PersonSerializer(items, many=True)
        return Response({"result":"Success","Data":serializer.data})

    def post(self,request,format=None):
        serializer = PersonSerializer(data=request.data)
        #validate existing data
        if Person.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self,request,pk=None,format=None):
        item = Person.objects.get(pk=pk)
        serialize = PersonSerializer(instance=item, data=request.data)
    
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk=None,format=None):
        item = get_object_or_404(Person,pk=pk)
        item.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

# display the blog
def display(request):
    lst=Person.objects.all()
    context = {'form':lst}
    return render(request,'display.html',context)