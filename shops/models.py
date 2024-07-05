from django.db import models
from django.core.exceptions import ValidationError

class City(models.Model):
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name


class Street(models.Model):
    street_name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.street_name} in {self.city}'


class Shop(models.Model):
    shop_name = models.CharField(max_length=50)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    home = models.CharField(max_length=5)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return self.shop_name

    def save(self, *args, **kwargs):
        if self.street.city != self.city:
            raise ValidationError('The street is not in the specified city.')
        super().save(*args, **kwargs)
