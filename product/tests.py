from rest_framework.test import APITestCase
from rest_framework import status


class ProductTestCase(APITestCase):

    def setUp(self):
        self.product_data = {
            "name": "test product",
            'sku': "test_product",
            "price": 9.99,
            "description": "test product description"
        }

        self.client.post('/api/product/', self.product_data, format="json")

    def test_get_proudct(self):
        response = self.client.get('/api/product/')
        self.assertIn('nr_of_users_want_it', response.data[0])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        response = self.client.post('/api/product/', self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_product(self):
        response = self.client.patch(
            '/api/product/1/', {"description": "a very cool product"})
        self.assertEqual(
            response.data["description"], "a very cool product")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        response = self.client.delete('/api/product/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
