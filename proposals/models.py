from django.db import models

class Proposal(models.Model):
    full_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=[('Aprovada', 'Aprovada'), ('Negada', 'Negada')], null=True)
