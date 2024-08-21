from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    number=models.IntegerField()
    email=models.EmailField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=100,  blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=True, default=0.00)
    available_since = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item1(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    available_since = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    contact_email = models.EmailField(max_length=254, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items1', default=1)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class item5(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    available_since = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    contact_email = models.EmailField(max_length=254, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    tags = models.ManyToManyField(Tag, related_name='items5', blank=True)
    quantity=models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name
    
    def is_stock(self):
        return self.quantity > 0
    is_stock.boolean=True

class itemimage(models.Model):
    image=models.ImageField(upload_to='C:\\Users\\hp\\Desktop\\ansh\\python training\\week6\\inventory\\inventory1\\img')    
    item=models.ForeignKey(item5,on_delete=models.CASCADE)
    def __str__(self):
        return f'Image for {self.item.name}'