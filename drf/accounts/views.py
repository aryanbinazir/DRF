from django.contrib.admin.templatetags.admin_list import pagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.core.paginator import Paginator

class UserRegister(APIView):
    def post(self, request):
        ser_user = UserRegisterSerializer(data=request.POST)
        if ser_user.is_valid():
            ser_user.create(ser_user.validated_data)
            return Response(ser_user.data, status=status.HTTP_201_CREATED)
        return Response(ser_user.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def list(self, request):
        page_number = request.GET.get('page', 1)
        page_size = request.GET.get('limit', 2)
        paginator = Paginator(self.queryset, page_size)
        srz_user = UserSerializer(instance=paginator.get_page(page_number), many=True)
        return Response(srz_user.data, status=status.HTTP_200_OK)

    def retrieve(self,request, pk=None):
        user = get_object_or_404(User, pk=pk)
        srz_user = UserSerializer(instance=user)
        return Response(srz_user.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        if user != request.user:
            return Response({'permission denied': 'You are not the owner'})
        srz_user = UserSerializer(instance=user, data=request.POST, partial=True)
        if srz_user.is_valid():
            srz_user.save()
            return Response(srz_user.data, status=status.HTTP_201_CREATED)
        return Response(srz_user.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        if user != request.user:
            return Response({'permission denied': 'You are not the owner'})
        user.is_active = False
        user.save()
        return Response({'message': f'user({user.username}) deactivated'}, status=status.HTTP_202_ACCEPTED)

class UserListApi(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

