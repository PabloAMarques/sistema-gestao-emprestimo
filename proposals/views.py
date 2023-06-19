from rest_framework import viewsets
from .models import Proposal
from .serializers import ProposalSerializer
from django.shortcuts import render, redirect
from .forms import ProposalForm

class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

def propostas(request):
    # Buscar todas as propostas do banco de dados
    propostas = Proposal.objects.all()
    # Criar um dicionário com as propostas para enviar para o template
    context = {
        'propostas': propostas,
    }
    return render(request, 'loans/proposal_form.html', context)

def create_proposal(request):
    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('propostas')
    else:
        form = ProposalForm()
    
    context = {'form': form}
    return render(request, 'loans/proposal_form.html', context)