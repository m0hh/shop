# Simple shop system

This is a simple shop system that contains four apps user, product, cart and orders

## Authentication

I used Token authentication to Verify users

## Database

We Used Postgresql

## Testing

We used pytest

## Project setup

Create a postgresql database

Copy the database credentials in the .env file

Create a secret_key and copy it to the .env file

Create a virtual env

Install required packages:

    pip3 install -r requirements.txt

Initialize database:

    python3 manage.py makemigrations
    python3 manage.py migrate

Run
pytest

to ensure every thing is working fine

## Documentation

### Registration

To register a user send a POST request to this url /register/ with a request like this

```
  {
      "username" : "test",
      "password" : "test4321"
  }
```

you will recive a response like this

```
  {
      "username": "test"
  }
```

### Authentication

To get Token to use for authentication send a POST request to this url /api-token-auth/
with this request

```
    {
      "username" : "test",
      "password" : "test4321"
    }
```

You will get a response like this

```
    {
       "token": "1e07db972135f27cc28a4930964ed693626aee91"
    }
```

You will use this token every time you send a request

### Create a Product

Send a POST request to this url /product/create/ with Token in headers under Authorization : Token {actual_token}

with request like this

```
   {
       "name": "Product1",
       "price": 1
   }
```

you will recive response like this

```
    {
        "id": 7,
        "name": "Product1",
        "price": 1,
        "owner": 5
    }
```

### List all the products

To see all the products send a GET request without the token to this url /product/list
you will receive a list of all the products orderd by price like this

```
[
    {
        "id": 5,
        "name": "aaaa11",
        "price": 1,
        "owner": 2
    },
    {
        "id": 7,
        "name": "Product1",
        "price": 1,
        "owner": 5
    },
    {
        "id": 6,
        "name": "aaaa11",
        "price": 1,
        "owner": 5
    },
    {
        "id": 1,
        "name": "btata",
        "price": 3,
        "owner": 2
    },
    {
        "id": 4,
        "name": "aaaa",
        "price": 4,
        "owner": 2
    },
    {
        "id": 2,
        "name": "a",
        "price": 5,
        "owner": 2
    },
    {
        "id": 3,
        "name": "aa",
        "price": 6,
        "owner": 2
    }
]
```

if you which to serch for a product by name just prefix the url with ?search=productname

### Add a product to my cart

Send a POST request with the token to this url /cart/add/

with a request containing the id of the product you wish to add to cart of the user who sent the request like this

```
{
    "product":5
}
```

you will receive a response like this

```
{
    "id": 2,
    "owner": 5,
    "products": [
        5
    ]
}
```

here we see owner is the id of the user who created the cart and products is list of all the products in the cart

### Remove a product from the cart

to remove a product from the cart send a POST request with the token to this url /cart/remove/
with a request with the id of product you wish to be removed

```
{
    "product":5
}
```

you will receive a response like this

```
{
    "id": 2,
    "owner": 5,
    "products": []
}
```

### Get a user's cart

to get a user's cart send a GET request with token in the headers to this url /cart/get/

you will receive a response like this

```
{
    "id": 2,
    "owner": 5,
    "products": []
}
```

### Create an order

to create an order with all the items in the cart send a POST request with the token to this url /order/create/
don't send add any data to the request body
you will recive a response with all the orders that just have been created like this

```
[
    {
        "id": 14,
        "owner": 5,
        "product": 1
    },
    {
        "id": 15,
        "owner": 5,
        "product": 2
    },
    {
        "id": 16,
        "owner": 5,
        "product": 3
    }
]
```

id is the id of the order
owner is the id of user who created the order
product is the id of the product

### List all orders

To list all orders that a user has created send a GET request with the token to this url /order/get/

you will recive a response like this

```
[
    {
        "id": 14,
        "owner": 5,
        "product": 1
    },
    {
        "id": 15,
        "owner": 5,
        "product": 2
    },
    {
        "id": 16,
        "owner": 5,
        "product": 3
    },
    {
        "id": 17,
        "owner": 5,
        "product": 5
    },
    {
        "id": 18,
        "owner": 5,
        "product": 6
    }
]
```
