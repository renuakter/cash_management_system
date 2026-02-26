from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthUserModel(AbstractUser):

    def __str__(self):
        return f'{self.username}'

class CashModel(models.Model):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE, null=True, related_name='user_cash')
    source = models.CharField(max_length=250, null=True)
    datetime = models.DateTimeField(null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10,null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.user.username}-{self.amount}'

class ExpenceModel(models.Model):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE, null=True, related_name='user_expense')
    datetime = models.DateTimeField(null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10,null=True)
    description = models.TextField(null=True)
    
    def __str__(self):
        return f'{self.user.username}-{self.amount}'
