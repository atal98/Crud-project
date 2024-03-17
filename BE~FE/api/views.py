from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.response import Response

class ProjectAPI(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

    def get(self, request, pk=None):

        if pk:
            queryset = Project.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
        else:
            queryset = Project.objects.all().order_by('-modified')
            serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    # def create(self,request):

    #     serializer = self.serializer_class(request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):  # Change 'create' to 'post'

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return status 201 for successful creation
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        queryset = Project.objects.get(id=pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        queryset = Project.objects.get(id=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)