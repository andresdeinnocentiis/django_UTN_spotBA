import pytest






@pytest.mark.products
@pytest.mark.django_db
def test_create_product(create_product):
    product = create_product
    print(product.name)
    assert product.name == "Producto 1"
    
    

@pytest.mark.django_db
def test_product_name(product):
    print(product.name)
    assert product.name == 'Test Product'
    
@pytest.mark.users   
@pytest.mark.django_db
def test_create_user(create_user):
    new_user = create_user
    print(new_user.username)
    assert new_user.username == "Andres"
















