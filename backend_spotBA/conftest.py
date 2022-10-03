from math import prod
import pytest
from base.models import Product, CustomUser, Category, Size, Brand, Model
import datetime
from faker import Faker

fake = Faker()


@pytest.fixture()
def create_product(db):
    product = Product(name='Producto 1', createdAt=datetime.datetime.now())
    product.save()
    
    return product


@pytest.fixture()
def create_product_factory(db):
    category = Category(name='Test Category')
    category.save()
    brand = Brand(name='Test Brand')
    brand.save()
    model = Model(name='Test Model')
    model.save()
    size = Size(size="L", size_type='UK', gender='M')
    size.save()
    
    def create_product(
        name = "Test Product",
        createdAt=datetime.datetime.now(),
        category = category,
        brand = brand,
        model = model,
        size = size,
        condition = 'DS',
        price = 55.2,
        currency = 'USD',
        stock = 5
    ):
        new_product = Product(
            name = name,
            createdAt=createdAt,
            category = category,
            brand = brand,
            model = model,
            size = size,
            condition = condition,
            price = price,
            currency = currency,
            stock = stock
        )
        new_product.save()
        
        return new_product
    
    return create_product


@pytest.fixture()
def product(db, create_product_factory):
    return create_product_factory(name=fake.name(), createdAt=fake.date())


@pytest.fixture()
def create_user(db):
    new_user = CustomUser(
        username='Andres', 
        email='andresdeinnocentiis@gmail.com',
        birthday=datetime.datetime.now(),
    )
    new_user.save()
    
    return new_user