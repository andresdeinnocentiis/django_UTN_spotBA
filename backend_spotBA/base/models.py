from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Address(models.Model):
    _id                 = models.AutoField(primary_key=True, editable=False)
    
    # Own attributes:
    address             = models.CharField(max_length=200, null=True, blank=True)
    city                = models.CharField(max_length=200, null=True, blank=True)
    zip_code            = models.CharField(max_length=50, null=True, blank=True)
    state               = models.CharField(max_length=200, null=True, blank=True)
    country             = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f'{self.address}, {self.city}, {self.state}, {self.country} - Zip Code: {self.zip_code}'
    

class Phone(models.Model):
    _id                 = models.AutoField(primary_key=True, editable=False)
    
    # Own attributes:
    mobile              = models.BooleanField(default=True)
    country_code        = models.IntegerField(default=54, null=False, blank=False)
    area_code           =  models.IntegerField(default=11, null=False, blank=False)
    number              =  models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return f'{self.country_code}{f"-9" if self.mobile else ""}-{self.area_code}-{self.number}'
    
class CustomUser(AbstractUser):
    
    # Foreign keys:
    phone               = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True, blank=False) # on delete CASCADE significa que si se borra el user, se borra lo que tiene asociado, en este caso, la Address
    address             = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=False)
    
    # Own attributes:
    email               = models.EmailField(unique=True)
    birthday            = models.DateField(blank=False, null=False)
    amount_purchases    = models.IntegerField(blank=True, null=True, default=0)
    money_spent         = models.DecimalField(max_digits=30, decimal_places=2, blank=True,null=True, default=0)
    shoe_size           = models.CharField(max_length=50, blank=True, null=True)
    upper_size          = models.CharField(max_length=50, blank=True, null=True)
    lower_size          = models.CharField(max_length=50, blank=True, null=True)
    
    
    
    
    def __str__(self):
        return self.username
class Brand(models.Model):
    _id                 = models.AutoField(primary_key=True, editable=False)
    name                = models.CharField(max_length=200, null=True, blank=True, unique=True)     
     
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    _id                 = models.AutoField(primary_key=True, editable=False)
    name                = models.CharField(max_length=200, null=True, blank=True, unique=True) 
     
    def __str__(self):
        return self.name
    


class Provider(models.Model):
    _id                 = models.AutoField(primary_key=True, editable=False)
    
    # Foreign Keys:
    phone               = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True, blank=True) # on delete CASCADE significa que si se borra el user, se borra lo que tiene asociado, en este caso, la Address
    address             = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    
    # Own attributes
    name                = models.CharField(max_length=50, blank=True, null=True)
    email               = models.EmailField(unique=False, blank=True, null=True)
    
    
    def __str__(self):
        return self.name


class Product(models.Model):
    _id                 = models.AutoField(primary_key=True, editable=False)
    
    # Foreign keys:
    user                = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True) # "on_delete=models.SET_NULL" significa que aunque se elimine el usuario, no se elimina lo que él creó (ej. los productos)
    category            = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand               = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True) 
    
    # Own attributes:
    name                = models.CharField(max_length=200, null=False, blank=False)
    size                = models.CharField(max_length=50, null=True, blank=True)
    SIZE_TYPES = (
        ('US', 'US'),
        ('W', 'W'),
        ('Y', 'Y'),
        ('GS', 'GS'),
        ('PS', 'PS'),
        ('XXS', 'XXS'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('UK', 'UK'),
        ('C', 'C'),
    )
    size_type           = models.CharField(max_length=10, choices=SIZE_TYPES, null=True, blank=True)
    colorway            = models.CharField(max_length=50, null=True, blank=True)
    CONDITIONS = (
        ('DS', 'DS'),
        ('VNDS', 'VNDS'),
        ('USED', 'USED'),
    )
    condition           = models.CharField(max_length=10, choices=CONDITIONS, null=True, blank=True)
    model               = models.CharField(max_length=50, null=True, blank=True)
    
    price               = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    CURRENCIES = (
        ('USD', 'USD'),
        ('ARS', 'ARS'),
    )
    currency            = models.CharField(max_length=3, choices=CURRENCIES, default='ARS', null=True, blank=False)
    image               = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    description         = models.TextField(null=True, blank=True)
    rating              = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews          = models.IntegerField(null=True, blank=True, default=0)
    stock               = models.IntegerField(null=True, blank=True, default=0)
    createdAt           = models.DateTimeField(auto_now_add=True)
    
     
    def __str__(self):
        return f'{self.name} / {self.brand if self.brand else "No brand"} / {self.model if self.model else "No model"} / {self.colorway if self.colorway else ""} / {self.size + " (" + self.size_type + ")" if self.size else ""} / {self.condition if self.condition else ""}'


class AcquirementsDetail(models.Model):
    _id                 = models.AutoField(primary_key=True, editable=False)
    
    # Foreign Keys:
    product             = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    provider            = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    
    # Own attributes:
    boughtAt            = models.DateTimeField()
    CURRENCIES = (
        ('USD', 'USD'),
        ('ARS', 'ARS'),
    )
    currency            = models.CharField(max_length=3, choices=CURRENCIES, default='USD', null=True, blank=True)
    boughtPrice         = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    STATUS = (
        ('IN STOCK', 'IN STOCK'),
        ('SOLD', 'SOLD'),
        ('STOLEN', 'STOLEN'),
        ('TRADED', 'TRADED'),
    )
    status              = models.CharField(max_length=20, choices=STATUS, default='IN STOCK', null=True, blank=True)
    LOCATIONS = (
        ('DROPS', 'DROPS'),
        ('ICECLUB', 'ICECLUB'),
        ('USA.NICKY', 'USA.NICKY'),
        ('SPOT 1', 'SPOT 1'),
        ('SPOT 2', 'SPOT 2'),
        ('SPOT 3', 'SPOT 3'),
    )
    location            = models.CharField(max_length=20, choices=LOCATIONS, null=True, blank=True)
    

class Review(models.Model):
    _id                 = models.AutoField(primary_key=True, editable=False)
    
    # Foreign keys:
    user                = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    product             = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True) 
    
    # Own attributes:
    title               = models.CharField(max_length=200, null=True, blank=True)
    rating              = models.IntegerField(null=True, blank=True, default=0)
    comment             = models.TextField(null=True, blank=True)
    createdAt           = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.rating)



class Order(models.Model):
    _id                 = models.AutoField(primary_key=True, editable=False)
    
    # Foreign keys:
    user                = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    
    # Own attributes:
    paymentMethod       = models.CharField(max_length=200, null=True, blank=True)
    taxPrice            = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice       = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice          = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid              = models.BooleanField(default=False)
    paidAt              = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered         = models.BooleanField(default=False)
    deliveredAt         = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt           = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.createdAt)



class OrderItem(models.Model):
    _id                 = models.AutoField(primary_key=True, editable=False) 
    
    # Foreign keys:
    product             = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order               = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    
    # Own attributes:
    name                = models.CharField(max_length=200, null=True, blank=True)
    qty                 = models.IntegerField(null=True, blank=True, default=0)
    price               = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image               = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name) # No hace falta convertirlo a String, pero igual lo convertimos por las dudas que el campo quede vacío



class ShippingAddress(models.Model):
    _id                 = models.AutoField(primary_key=True, editable=False)
    
    # Foreign keys:
    # ACA EN ORDER USAMOS ONE TO ONE FIELD, xq para 1 Order hay 1 ShippingAddress, y para 1 ShippingAddress hay 1 Order
    order               = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True) # on delete CASCADE significa que si se borra la orden, se borra lo que tiene asociado, en este caso, la Shipping Address
    
    # Own attributes:
    address             = models.CharField(max_length=200, null=True, blank=True)
    city                = models.CharField(max_length=200, null=True, blank=True)
    zip_code            = models.CharField(max_length=200, null=True, blank=True)
    state               = models.CharField(max_length=200, null=True, blank=True)
    country             = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice       = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return str(self.address)



















