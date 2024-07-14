from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from catalog.models import Product
from catalog.tests.helpers import sample_category, sample_product


class ProductAPITests(APITestCase):
    def test_create_product(self):
        category = sample_category()
        url = reverse("catalog:products-list")
        data = {
            "name": "Test Product",
            "description": "This is a test product",
            "price": 10.99,
            "category": category.id,
            "stock": 100,
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Product.objects.filter(name="Test Product").exists())

    def test_list_products(self):
        url = reverse("catalog:products-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        product = sample_product()
        url = reverse("catalog:products-detail", kwargs={"pk": product.pk})
        data = {"price": 100}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.price, 100)

    def test_delete_product(self):
        product = sample_product()
        url = reverse("catalog:products-detail", kwargs={"pk": product.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(pk=product.pk).exists())
