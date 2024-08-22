from django.db import models
class Product(models.Model):
 name = models.CharField(max_length=255)
 price = models.IntegerField()
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    ident = models.CharField(max_length=100)  # Assuming ident is a CharField

    def __str__(self):
        return f"Comment by {self.ident} on {self.product.name}"
# Create your models here.
