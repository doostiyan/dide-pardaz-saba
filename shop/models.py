from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Mobile(models.Model):
    STATUS_CHOICES = [
        ('+', '+'),
        ('-', '-'),
    ]

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100, unique=True)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=100)
    screen_size = models.DecimalField(max_digits=3, decimal_places=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    manufacture_country = models.CharField(max_length=100)

    def __str__(self):
        return self.model