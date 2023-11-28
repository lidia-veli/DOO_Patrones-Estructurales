from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def calculate_price(self):
        return self.price


class Menu(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    items = models.ManyToManyField(MenuItem, through='MenuComposition')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def calculate_price(self):
        return sum(item.calculate_price() for item in self.items.all())


class MenuComposition(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
