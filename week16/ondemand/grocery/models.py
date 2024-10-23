from django.db import models
 
 
 
class timestamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
 
 
class usertable(timestamps):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    new_password=models.CharField(max_length=50)
    phone_number=models.IntegerField(max_length=10,unique=True)
    address=models.CharField(max_length=100)
 
    def __str__(self):
        return self.name
    
 
 
 
class SupplierStore(timestamps):
    store_owner = models.IntegerField()
    store_name = models.CharField(max_length=255)
    store_mail = models.EmailField()
    store_contact = models.CharField(max_length=15)
    store_image = models.BinaryField(null=True, blank=True)
    store_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
 
 
class Product(timestamps):
    store = models.ForeignKey(SupplierStore, on_delete=models.CASCADE)
    prod_image = models.BinaryField()
    prod_name = models.CharField(max_length=255)
    prod_desc = models.TextField()
    prod_subcat = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
 
class Category(timestamps):
    category_image = models.BinaryField()
    category_title = models.CharField(max_length=255)
 
class SubCategory(timestamps):
    subcategory_title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
 
class CustomerRating(timestamps):
    store = models.ForeignKey(SupplierStore, on_delete=models.CASCADE)
    customer_rating = models.DecimalField(max_digits=3, decimal_places=2)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
 
 
class UserTable(timestamps):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    password = models.TextField()
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
 
class Order(timestamps):
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
 
class OrderItem(timestamps):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
 
class Address(timestamps):
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
 
 
class Transaction(timestamps):
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    trans_amount = models.DecimalField(max_digits=10, decimal_places=2)
    trans_date_time = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    shipping_address = models.TextField()
 
 
 
class ContactUs(timestamps):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(null=True, blank=True)
 
 
class Notification(timestamps):
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    message = models.TextField()
    notif_type = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
 
 
class Faq(timestamps):
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
 
class PromoCode(timestamps):
    promo_name = models.CharField(max_length=50)
    promo_discount = models.DecimalField(max_digits=5, decimal_places=2)
    promo_validity = models.DateTimeField()
 