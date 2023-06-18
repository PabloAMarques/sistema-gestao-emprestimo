from django.contrib import admin
from .models import Proposal

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'cpf', 'address', 'loan_amount', 'status')
