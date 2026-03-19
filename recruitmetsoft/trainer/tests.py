from rest_framework import status
from rest_framework.test import APITestCase

from .models import Trainer


class TrainerAuthenticationTests(APITestCase):
    def setUp(self):
        self.login_url = '/trainer/login/'
        self.list_url = '/trainer/get_trainer/'
        self.create_url = '/trainer/add_trainer/'
        self.refresh_url = '/api/token/refresh/'
        self.trainer_payload = {
            'username': 'trainer1',
            'password': 'StrongPass123!',
            'name': 'Amit Kumar',
            'contact': '9876543210',
            'address': 'Kolkata',
            'tech_stack': 'Python, Django, REST',
            'total_experience': '3.5',
        }

    def test_add_trainer_hashes_password(self):
        response = self.client.post(self.create_url, self.trainer_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotIn('password', response.data)
        self.assertEqual(Trainer.objects.count(), 1)
        self.assertNotEqual(Trainer.objects.get().password, self.trainer_payload['password'])

    def test_login_returns_jwt_tokens(self):
        self.client.post(self.create_url, self.trainer_payload, format='json')
        response = self.client.post(
            self.login_url,
            {'username': 'trainer1', 'password': 'StrongPass123!'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.data['trainer']['username'], self.trainer_payload['username'])

    def test_trainer_list_requires_authentication(self):
        list_response = self.client.get(self.list_url, format='json')

        self.assertEqual(list_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_list_trainers(self):
        self.client.post(self.create_url, self.trainer_payload, format='json')
        login_response = self.client.post(
            self.login_url,
            {'username': 'trainer1', 'password': 'StrongPass123!'},
            format='json',
        )
        access_token = login_response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        list_response = self.client.get(self.list_url, format='json')

        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(Trainer.objects.count(), 1)
        self.assertEqual(list_response.data[0]['username'], self.trainer_payload['username'])
        self.assertNotIn('password', list_response.data[0])

    def test_refresh_token_returns_new_access_token(self):
        self.client.post(self.create_url, self.trainer_payload, format='json')
        login_response = self.client.post(
            self.login_url,
            {'username': 'trainer1', 'password': 'StrongPass123!'},
            format='json',
        )

        refresh_response = self.client.post(
            self.refresh_url,
            {'refresh': login_response.data['refresh']},
            format='json',
        )

        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertIn('access', refresh_response.data)
