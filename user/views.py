"""
User views
"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


@api_view(["GET"])
def get_users(request):
    try:
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception:
        return Response({'message': "Interval Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def get_single_user(request, user_id):

    serializer = UserSerializer(data=request.data)
    try:
        if serializer.is_valid():
            user = User.objects.get(id=user_id)
            serialized_user = UserSerializer(user)
            return Response(serialized_user.data, status=status.HTTP_200_OK)
        return Response({'message': 'Id does not exist'}, status=status.HTTP_204_NO_CONTENT)
    except Exception:
        return Response({'message': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
