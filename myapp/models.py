from django.db import models


# Create your models here.

class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    address=models.TextField()
    password= models.CharField(max_length=100)
    usertype= models.CharField(max_length=100,default='buyer')
    

    def __str__(self):
        return self.fname+''+self.lname
        
class Product(models.Model):
    seller= models.ForeignKey(User,on_delete=models.CASCADE)
    brand=(
        ("puma","puma"),
        ("nike","nike"),
        ("addidas","addidas"),
        ("bata","bata"),
    )   
    size=(
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
        ("11","11"),
        

    )
    Product_brand= models.CharField(max_length=100,choices=brand)
    product_price=models.PositiveIntegerField()
    product_size= models.CharField(max_length=100,choices=size)
    product_pic=models.ImageField(upload_to="product_pic/")
    
    def __str__(self):
        return self.seller.fname+' '+self.Product_brand
        
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.fname+" - " +self.product.Product_brand


    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_price=models.PositiveIntegerField()
    product_qty= models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    payment_status = models.BooleanField(default= False)
    def __str__(self) -> str:
        return self.user.fname+" - " +self.product.Product_brand

