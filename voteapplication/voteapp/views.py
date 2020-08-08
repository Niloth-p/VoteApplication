from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Candidate

def index(request):
    if request.method == 'POST':
        results()
    latest_candidate_list = Candidate.objects.order_by('-name')
    context = {'latest_candidate_list': latest_candidate_list}
    return render(request, 'voteapp/index.html', context)

def detail(request, candidate_id):
    cand = get_object_or_404(Candidate, pk=candidate_id)
    return render(request, 'voteapp/detail.html', {'cand': cand})

def results(request):
    cand_id = request.POST.get('vote_for')
    print(cand_id)
    cand = Candidate.objects.get(pk=cand_id)
    print(cand.votes)
    cand.votes = cand.votes+1
    print(cand.votes)
    cand.save()
    latest_candidate_list = Candidate.objects.order_by('-name')
    context = {'latest_candidate_list': latest_candidate_list}
    return render(request, 'voteapp/results.html', context)

