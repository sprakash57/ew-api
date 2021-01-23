"""
User views
"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from .models import User
from .serializers import UserSerializer


@api_view(["GET"])
def get_users(request):
    try:
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as err:
        return Response({'message': str(err)}, status=status.HTTP_404_NOT_FOUND)
    # except DatabaseError:
    #     return Response(
    #         {'message': "Interval Server Error"},
    #         status=status.HTTP_500_INTERNAL_SERVER_ERROR
    #     )


@api_view(["GET", "DELETE", "PUT"])
def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        s_user = UserSerializer(user)
        if request.method == 'GET':
            return Response(s_user.data, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            user.delete()
            response = {'message': f'${s_user.data.name} has been deleted'}
            return Response(response, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            update_srializer = UserSerializer(user, data=request.data)
            if update_srializer.is_valid():
                update_srializer.save()
                return Response(update_srializer.data, status=status.HTTP_200_OK)
            return Response({'message': update_srializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist as err:
        return Response({'message': str(err)}, status=status.HTTP_404_NOT_FOUND)
    except DatabaseError:
        return Response(
            {'message': 'Internal server error'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["POST"])
def create_user(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except DatabaseError:
        return Response(
            {'message': 'Internal Server Error'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
