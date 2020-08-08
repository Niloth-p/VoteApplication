from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Candidate, VotedIP
import datetime
from django.conf import settings


def index(request):
    curr_ip = get_client_ip(request)
    voted_ips = VotedIP.objects.filter(ip_address__contains=curr_ip)
    if voted_ips:
        return results(request)
    else:
        latest_candidate_list = Candidate.objects.order_by('-name')
        context = {'latest_candidate_list': latest_candidate_list}
        return render(request, 'voteapp/index.html', context)


def detail(request, candidate_id):
    cand = get_object_or_404(Candidate, pk=candidate_id)
    return render(request, 'voteapp/detail.html', {'cand': cand})


def results(request):
    if request.method == 'POST':
        cand_id = request.POST.get('vote_for')
        cand = Candidate.objects.get(pk=cand_id)
        cand.votes = cand.votes+1
        cand.save()
        save_client_ip(get_client_ip(request))
    latest_candidate_list = Candidate.objects.order_by('-name')
    context = {'latest_candidate_list': latest_candidate_list}
    return render(request, 'voteapp/results.html', context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def save_client_ip(ipaddress):
    get_ip = VotedIP()
    get_ip.ip_address= ipaddress
    get_ip.pub_date = datetime.date.today() 
    get_ip.save()

