from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from authentication.models import Profile
from authentication.serializers import ProfileSerializer


class ProfileAPITests(APITestCase):
    def test_create_profile(self):
        data = {
            "user": {
                "username": "test_user",
                "email": "test@example.com",
                "password": "test_password",
            }
        }
        response = self.client.post("/authentication/profiles/", data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_retrieve_profiles(self):
        user = User.objects.create(username="XXXXXXXXX", email="test@example.com")
        Profile.objects.create(user=user)

        response = self.client.get("/authentication/profiles/")
        self.assertEqual(response.status_code, 200)

    def test_update_profile(self):
        user = User.objects.create(username="XXXXXXXXX", email="test@example.com")
        profile = Profile.objects.create(user=user)

        data = {"user": {"username": "updated_username"}}
        response = self.client.patch(
            f"/authentication/profiles/{profile.id}/", data, format="json"
        )
        self.assertEqual(response.status_code, 200)

    def test_profile_serializer(self):
        user = User.objects.create(username="test_user", email="test@example.com")
        profile = Profile.objects.create(user=user)
        serializer = ProfileSerializer(instance=profile)
        expected_data = {
            "id": profile.id,
            "user": {"id": user.id, "username": user.username, "email": user.email},
        }
        self.assertEqual(serializer.data, expected_data)
