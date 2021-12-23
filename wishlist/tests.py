from rest_framework.test import APITestCase
from rest_framework import status

from user.models import User


class WishlistTestCase(APITestCase):

    def setUp(self):

        self.client.post('/api/user/register/', {'email': 'test@test.com',
                                                 'password': 'test1234', 'first_name': 'test', 'last_name': 'test'})
        user = User.objects.get(email='test@test.com')
        self.client.force_authenticate(user=user)
        self.product_data = {
            "name": "test wishlist",
        }
        self.client.post('/api/wishlist/', self.product_data, format="json")

        self.product_data = {
            "name": "test product",
            'sku': "test_product",
            "price": 9.99,
            "description": "test product description"
        }

        self.client.post('/api/product/', self.product_data, format="json")

    def test_get_wishlist(self):
        self.client.login(email='test@test.com', password='test1234')
        response = self.client.get('/api/wishlist/')
        self.assertIn('owner', response.data[0])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_wishlist(self):
        response = self.client.post(
            '/api/wishlist/', {"name": "test wishlist"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_product(self):
        response = self.client.patch(
            '/api/wishlist/1/', {"name": "my favourite wishlist"})
        self.assertEqual(
            response.data["name"], "my favourite wishlist")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_wishlist(self):
        response = self.client.delete('/api/wishlist/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_add_to_wishlist(self):
        response = self.client.post('/api/wishlist/1/add/', {"product": 1})
        wishlist = self.client.get('/api/wishlist/1/')
        self.assertEqual(len(wishlist.data['product']), 1)
        self.assertEqual(response.data['message'],
                         "Product successfully added to wishlist.")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_remove_from_wishlist(self):
        self.client.post('/api/wishlist/1/add/', {"product": 1})

        response = self.client.delete(
            '/api/wishlist/1/remove/', {"product": 1})
        wishlist = self.client.get('/api/wishlist/1/')
        self.assertEqual(len(wishlist.data['product']), 0)
        self.assertEqual(response.data['message'],
                         "Product successfully removed from wishlist.")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
