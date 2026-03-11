from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Institute
from .serializers import InstituteSerializer

@api_view(['GET'])
def get_institutes(request):
    institutes = Institute.objects.all().values()
    return Response(list(institutes))


@api_view(['POST'])
def add_institute(request):

    serializer = InstituteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)
