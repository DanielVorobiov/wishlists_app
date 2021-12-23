# Run app
Create a virtualenv and then use `pip install -r requirments.txt` to install the requirments.
Use `manage.py runserver` to run the application.
For testing purposes of this app I used Basic Auth and created 2 accounts that you can use for testing:
- email: test@test.com, password: test1234
- email: fotest@test.com, password: test1234

You can use `http://127.0.0.1:8000/api/user/register/` to register a new use with form data:
- first_name
- last_name
- email
- password

# Endpoints
- login: `http://127.0.0.1:8000/api/user/login/` 
- Create product: `http://127.0.0.1:8000/api/product/` 
- List products: `http://127.0.0.1:8000/api/product/` 
- Update product: `http://127.0.0.1:8000/api/product/id/` 
- Delete product: `http://127.0.0.1:8000/api/product/id/` 
- Create wishlist: `http://127.0.0.1:8000/api/wishlist/`
- List wishlists: `http://127.0.0.1:8000/api/wishlist/`
- Update wishlist: `http://127.0.0.1:8000/api/wishlist/id/`
- Delete wishlist: `http://127.0.0.1:8000/api/wishlist/id/`
- Add Product to ishlist: `http://127.0.0.1:8000/api/wishlist/id/add/`
- Delete Produt from wishlist: `://127.0.0.1:8000/api/wishlist/9/remove/`

# Unit tests
There are severeal tests for every endpoin of the app. Use `manage.py test` to run the tests.