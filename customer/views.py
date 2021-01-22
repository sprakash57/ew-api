"""
Customer views
"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .serializers import DetailsSerializer
from .models import Details
# Create your views here.


@api_view(["GET"])
def get_details(request):
    """
    API to register new customers
    """
    customers = Details.objects.all()
    serializer = DetailsSerializer(customers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def createDetails(request):
    """
    API to register new customers
    """
    serializer = DetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def deleteDetails(request, cust_id):
    customer = Details.objects.get(id=cust_id)
    try:
        customer.delete()
        return Response({'message': f'Customer {cust_id} deleted'}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'message': 'Customer not found'}, status=status.HTTP_204_NO_CONTENT)
    except Exception:
        return Response({'message': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
