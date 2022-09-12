from django.contrib import admin
from .models import CustomUser, Provider, Brand, Category, Product, Address, Phone, ShippingAddress, Review, Order, OrderItem, AcquirementsDetail


class ProductInline(admin.TabularInline):
     model = Product
     extras = 0
     

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General Info', {
            'fields': [
                'user', 'name', 'model', 'colorway', 'condition', 'currency', 'price', 'stock', 'description', 
            ]
        }),
        ('Size', {
            'fields': [
                'size_type', 'size', 
            ]
        }),
        ("Relationship", {
            'fields':[
            'brand', 'category'
            ]
        }),
        ('Image',{
            'fields':[
                'image'
            ]
        }),
        ('Other info',{
            'fields':[
                'rating', 'numReviews'
            ]
        }),
        
    ]
    list_display = ['_id','name', 'brand', 'model', 'colorway','size', 'size_type', 'currency', 'price', 'stock', 'description', 'category', 'image', 'rating', 'numReviews','user']
    list_filter = ('name', 'brand', 'price', 'category', 'rating', 'stock', 'numReviews','size', 'size_type',)
    search_fields = ('name', 'brand', 'price', 'category', 'rating', 'stock', 'numReviews','size', 'size_type',)
    ordering = ['_id']

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username','first_name', 'last_name', 'email', 'birthday', 'address', 'phone', 'amount_purchases', 'money_spent', 'shoe_size', 'upper_size', 'lower_size']
    list_filter = ('username', 'email', 'address', 'amount_purchases', 'money_spent', 'shoe_size', 'upper_size', 'lower_size', )
    search_fields = ('username', 'email', 'address', 'amount_purchases', 'money_spent', 'shoe_size', 'upper_size', 'lower_size',)
    ordering = ['id']
    

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['_id', 'name', 'email', 'address', 'phone']
    list_filter = ('name', 'email', 'address', )
    search_fields = ('name', 'email', 'address',)
    ordering = ['_id']

@admin.register(AcquirementsDetail)
class AcquirementsDetailAdmin(admin.ModelAdmin):
    list_display = ['_id', 'product_id', 'product','provider', 'boughtAt', 'boughtPrice']
    list_filter = ('product_id','product',  'provider', 'boughtAt', 'boughtPrice', )
    search_fields = ('product_id','product', 'provider', 'boughtAt', 'boughtPrice', )
    ordering = ['_id']


@admin.register(Address)    
class AddressAdmin(admin.ModelAdmin):
    list_display = ['_id','address', 'city', 'state', 'country', 'zip_code']
    list_filter = ('address', 'city', 'state', 'country', 'zip_code',)
    search_fields = ('address', 'city', 'state', 'country', 'zip_code',)
    ordering = ['_id']

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['_id','mobile', 'country_code', 'area_code', 'number']
    list_filter = ('mobile', 'country_code', 'area_code', )
    search_fields = ('mobile', 'country_code', 'area_code',)
    ordering = ['_id']

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['_id','order', 'address', 'city', 'state', 'country', 'zip_code', 'shippingPrice']
    list_filter = ('order', 'address', 'city', 'state', 'country', 'zip_code',)
    search_fields = ('order', 'address', 'city', 'state', 'country', 'zip_code',)
    ordering = ['_id']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['_id','user', 'paymentMethod', 'taxPrice', 'shippingPrice', 'totalPrice', 'isPaid', 'paidAt', 'isDelivered', 'deliveredAt', 'createdAt']
    list_filter = ('user', 'paymentMethod', 'isPaid', 'isDelivered', 'createdAt',)
    search_fields = ('user', 'paymentMethod', 'isPaid', 'isDelivered', 'createdAt',)
    ordering = ['_id']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['_id','product', 'order', 'name', 'qty', 'price', 'image']
    list_filter = ('product', 'order', 'name', )
    search_fields = ('product', 'order', 'name', )
    ordering = ['_id']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['_id','name']
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ['_id']
    inlines = [ProductInline]

@admin.register(Category) 
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['_id','name']
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ['_id']
    

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['_id', 'user', 'product', 'title', 'rating', 'createdAt', 'comment']
    list_filter = ('user','product','rating', )
    search_fields = ('user','product','rating', )
    ordering = ['_id']
    


