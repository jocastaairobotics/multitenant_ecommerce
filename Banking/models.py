from django.db import models


class Account(models.Model):
    account_number = models.CharField(max_length=5)
    account_holder = models.CharField(max_length=50)
    account_balance = models.IntegerField(default=0)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.account_holder