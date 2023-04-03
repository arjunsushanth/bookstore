from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    book_price = serializers.SerializerMethodField()

    def get_book_price(self, obj):
        return obj.price_currency +' ' +str(obj.price)

    class Meta:
        model = Book
        fields = (  'id',
                    'title', 
                    'description', 
                    'author', 
                    'cover_image',
                    'book_price',
                    )

class BookAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    #     title = models.CharField(max_length=200, unique=True, db_index=True)
    # description = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # cover_image = CloudinaryField(blank=True, null=True) #cloudnary field to store images in cloudnary cloud
    # price = models.PositiveIntegerField()
    # price_currency = models.CharField(max_length=500, default='EUR', choices=CURRENCIES)
    # created_at = models.DateTimeField(auto_now_add=True, blank=True)
    # updated_at