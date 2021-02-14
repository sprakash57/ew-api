from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from .models import Registration
from .serializers import RegSerializer


@api_view(["POST"])
def register(request):
    try:
        serializer = RegSerializer(data=request.data)
        if serializer.is_valid():
            for instance in Registration.objects.all():
                if instance.email == serializer.validated_data["email"].lower() and instance.email != "":
                    raise ValidationError("Email already exists")
                elif instance.phone == serializer.validated_data.get("phone") and instance.phone != "":
                    raise ValidationError("Phone number alreay exists")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except ValidationError as err:
        return Response({"message": err}, status=status.HTTP_409_CONFLICT)
    except Exception as err:
        return Response({"message": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
