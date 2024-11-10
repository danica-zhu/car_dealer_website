# pylint: disable=missing-class-docstring
# Uncomment the following imports before adding the Model code
# dsadsadsadasdsadasda
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# change
# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:


class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)  # 汽车品牌名称
    description = models.TextField()  # 描述信息
    country = models.CharField(max_length=50, blank=True, null=True)  # 制造国家

    def __str__(self):
        return f"{self.name} ({self.country})"  # 返回名称和国家作为字符串表示
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    # dealer_id = models.IntegerField()  # 经销商ID，参考Cloudant数据库中的经销商
    dealer_id = models.IntegerField(null=True, blank=True)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    # Other fields as needed

    def __str__(self):
        # return self.name  # Return the name as the string representation
        return f"{self.car_make.name} {self.name} ({self.year})"

# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
