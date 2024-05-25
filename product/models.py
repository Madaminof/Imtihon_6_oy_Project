from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from autentification.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categor'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    class Meta:
        db_table = 'gulcha'

    def __str__(self):
        return f"{self.name}  {self.category.name} "


class Review(models.Model):
    comment = models.CharField(max_length=128)
    star_given = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    gul = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f"{self.comment} - {self.star_given} "




class BatafsilMalumot(models.Model):
    first_name = models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    product= models.ForeignKey(Products, on_delete=models.CASCADE)

    class Meta:
        db_table = 'batafsil_malumot'




