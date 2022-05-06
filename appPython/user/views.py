from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from user.models import Users
from user.serializers import UserSerializer, UserJWTSerializer
from rest_framework.decorators import api_view, action

class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserJWTSerializer
    queryset = Users.objects.all()

    @swagger_auto_schema(request_body=UserSerializer)
    @action(detail=True, methods=['post'])
    def post(self, request):
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={200: UserSerializer(many=True)})
    @action(detail=True, methods=['get'])
    def get(self, request, pk=None): 
        if pk != None:
            # find user by Id
            try:
                user = Users.objects.get(pk=pk)
            except Users.DoesNotExist:
                return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
            
            if request.method == 'GET':
                user_serializer = UserSerializer(user)
                return JsonResponse(user_serializer.data)
        else:
            user = Users.objects.all()
            name = request.GET.get('name', None)
            if name is not None:
                user = user.filter(name_icontains=name)
            
            user_serializer = UserSerializer(user, many=True)
            return JsonResponse(user_serializer.data, safe=False)
    
    @swagger_auto_schema(responses={204: 'NO_CONTENT'})
    @action(detail=True, methods=['delete'])
    def delete(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    @swagger_auto_schema(request_body=UserSerializer)
    @action(detail=True, methods=['put'])
    def put(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 