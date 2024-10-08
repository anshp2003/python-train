from django.db import models

# Create your models here.


class category_model(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.name
    


class product_model(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)    
    category_model = models.ForeignKey(category_model, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True, blank=True)


    def __str__(self):
        return self.title
    


class order_model(models.Model):
    product_model= models.ForeignKey(product_model,related_name='orders', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def __str__(self):
        return f"{self.quantity} of {self.product.title} (Status: {self.status})"