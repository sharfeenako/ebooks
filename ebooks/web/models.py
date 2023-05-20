from django.db import models
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField



class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Lang_Category(models.Model):
    language=models.CharField(max_length=200) 

    def __str__(self):
        return self.language

class Book(models.Model):
    book_category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    language=models.ForeignKey(Lang_Category, on_delete=models.CASCADE)
    year=models.CharField(max_length=50)
    book_name=models.CharField(max_length=200)
    book_image=VersatileImageField(upload_to='book_image')
    book_hoverimage=VersatileImageField(upload_to='book_image')
    author_name=models.CharField(max_length=100)
    del_price=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    file=models.FileField(upload_to='books')
    details=models.TextField()
    describtion=models.TextField()

    def __str__(self):
        return self.book_name




