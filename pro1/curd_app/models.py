from django.db import models


class Food(models.Model):
    food_type = [("TEA", "tea"), ("PULAV", "pulav"), ("PAV BHAJI", "pav bhaji"),("COLD COFFEE", "cold coffee")]
    pay = [("ONLINE", "online"), ("CASH", "cash")]
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    food = models.CharField(max_length=20, choices=food_type)
    payment = models.CharField(max_length=20, choices=pay)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
