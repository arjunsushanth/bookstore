from django.db import models
from apps.users.models import User
from cloudinary.models import CloudinaryField

'''
I used cloudinary field to store the images.
We can store images in any other cloude like AWS S3. 
Since S3 is costly I used free cloud storage cloudinary to store book cover images.
'''

CURRENCIES = (
    ('EUR', 'EUR'),
    ('USD', 'USD'),
    ('INR', 'INR'),
)

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True, db_index=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = CloudinaryField(blank=True, null=True) #cloudnary field to store images in cloudnary cloud
    price = models.PositiveIntegerField()
    price_currency = models.CharField(max_length=500, default='EUR', choices=CURRENCIES)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    

