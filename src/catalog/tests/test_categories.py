from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from catalog.models import Category
from catalog.tests.helpers import sample_category


class CategoryAPITests(APITestCase):
    def test_create_category(self):
        url = reverse("catalog:categories-list")
        data = {
            "name": "Test Category",
            "parent": None,
            "children": [],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Category.objects.filter(name="Test Category").exists())

    def test_list_categories(self):
        url = reverse("catalog:categories-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_category(self):
        category = sample_category()
        url = reverse("catalog:categories-detail", kwargs={"pk": category.pk})
        data = {"name": "Updated Category"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category.refresh_from_db()
        self.assertEqual(category.name, "Updated Category")

    def test_delete_category(self):
        category = sample_category()
        url = reverse("catalog:categories-detail", kwargs={"pk": category.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(pk=category.pk).exists())
