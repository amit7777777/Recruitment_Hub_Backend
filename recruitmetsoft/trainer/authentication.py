from rest_framework import exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Trainer


class TrainerJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        trainer_id = validated_token.get('trainer_id')
        if not trainer_id:
            raise exceptions.AuthenticationFailed('Token contained no recognizable trainer identifier.')

        try:
            trainer = Trainer.objects.get(id=trainer_id)
        except Trainer.DoesNotExist as exc:
            raise exceptions.AuthenticationFailed('Trainer not found.') from exc

        if not trainer.is_active:
            raise exceptions.AuthenticationFailed('Trainer is inactive.')

        return trainer
