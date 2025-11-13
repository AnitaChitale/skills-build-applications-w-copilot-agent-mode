from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Workout, Activity, Leaderboard

class APISmokeTest(APITestCase):
	def test_api_root(self):
		url = reverse('api-root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_users_endpoint(self):
		url = '/api/users/'
		response = self.client.get(url)
		self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_403_FORBIDDEN])

	def test_teams_endpoint(self):
		url = '/api/teams/'
		response = self.client.get(url)
		self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_403_FORBIDDEN])

	def test_workouts_endpoint(self):
		url = '/api/workouts/'
		response = self.client.get(url)
		self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_403_FORBIDDEN])

	def test_activities_endpoint(self):
		url = '/api/activities/'
		response = self.client.get(url)
		self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_403_FORBIDDEN])

	def test_leaderboard_endpoint(self):
		url = '/api/leaderboard/'
		response = self.client.get(url)
		self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_403_FORBIDDEN])
