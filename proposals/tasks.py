from celery import shared_task
from .models import Proposal
from random import choice

@shared_task
def evaluate_proposal(proposal_id):
    proposal = Proposal.objects.get(id=proposal_id)
    proposal.status = choice(['Aprovada', 'Negada'])
    proposal.save()
