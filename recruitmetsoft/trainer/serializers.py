from rest_framework import serializers
from django.contrib.auth.hashers import check_password, make_password

from .models import Trainer


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = (
            'id',
            'username',
            'password',
            'name',
            'contact',
            'address',
            'tech_stack',
            'total_experience',
            'is_active',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class TrainerLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, trim_whitespace=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            trainer = Trainer.objects.get(username=username)
        except Trainer.DoesNotExist as exc:
            raise serializers.ValidationError('Invalid username or password.') from exc

        if not check_password(password, trainer.password):
            raise serializers.ValidationError('Invalid username or password.')

        if not trainer.is_active:
            raise serializers.ValidationError('Trainer account is inactive.')

        attrs['trainer'] = trainer
        return attrs
