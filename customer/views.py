from .models import Details
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DetailsSerializer

# Create your views here.
@api_view(["POST"])
def CreateDetails(request):
    """
    API to register new customers
    """
    serializer = DetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
