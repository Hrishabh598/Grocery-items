from django.db import models


from django.contrib.auth.models import User
# Create your models here.
class Items(models.Model):
    id=models.AutoField(primary_key=True)
    image=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    price=models.DecimalField(decimal_places=2,max_digits=3)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name




# class Orders(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     items_json = models.CharField(max_length=5000)
#     price = models.DecimalField(decimal_places=2,max_digits=12)
#     name = models.CharField(max_length=200)


# #cart
# class Cart(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='carts')
#     is_paid = models.BooleanField(default=False)

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cartItem')
#     item = models.ForeignKey(Items,on_delete=models.SET_NULL,null=True,blank=True)
