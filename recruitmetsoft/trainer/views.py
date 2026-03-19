from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Trainer
from .serializers import TrainerSerializer, TrainerLoginSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def trainer_login(request):
    serializer = TrainerLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    trainer = serializer.validated_data['trainer']
    refresh = RefreshToken()
    refresh['trainer_id'] = trainer.id
    refresh['username'] = trainer.username

    return Response(
        {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'trainer': {
                'id': trainer.id,
                'username': trainer.username,
                'name': trainer.name,
            },
        },
        status=status.HTTP_200_OK,
    )


@api_view(['GET'])
def get_trainers(request):
    trainers = Trainer.objects.all().order_by('id')
    serializer = TrainerSerializer(trainers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def add_trainer(request):
    serializer = TrainerSerializer(data=request.data)

    if serializer.is_valid():
        trainer = serializer.save()
        response_serializer = TrainerSerializer(trainer)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
