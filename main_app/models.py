from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('grain','GRAIN'),
    ('vegetables', 'VEGETABLES'),
    ('fruits','FRUITS'),
    ('dairy','DAIRY'),
    ('meat','MEAT'),
    ('misc','MISCELLANEOUS')
)

# Create your models here.
<<<<<<< HEAD

=======
CATEGORY_CHOICES = (
    ('grain','GRAIN'),
    ('vegetables', 'VEGETABLES'),
    ('fruits','FRUITS'),
    ('dairy','DAIRY'),
    ('meat','MEAT'),
    ('misc','MISCELLANEOUS')
)
# Create your models here.
>>>>>>> e3cab28354c0520a69cf37d35928e59aff68ae6a
class Post(models.Model):
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='grain')
    itemName = models.CharField(max_length=100)
    weightQuantity = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
<<<<<<< HEAD

    def __str__(self):
         return self.itemName
=======
    
    def __str__(self):
        return self.itemName
>>>>>>> e3cab28354c0520a69cf37d35928e59aff68ae6a
