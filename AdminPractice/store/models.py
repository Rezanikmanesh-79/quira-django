from django.db import models


class Address(models.Model):
    postal_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return '{}, {}'.format(self.city, self.postal_address)


class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}, {}'.format(self.name, self.company)
