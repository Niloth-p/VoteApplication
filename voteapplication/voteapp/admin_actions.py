from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Candidate, VotedIP
import datetime
from django.conf import settings


def add_cand(request):
    cand = Candidate()
    print(settings.ADMIN_AUTH_CODE)
    print(request.POST.get('data', ''))
    print(request.POST.get('authcode', ''))

    if request.POST.get('authcode', '') == settings.ADMIN_AUTH_CODE:
        cand.name = request.POST.get('name', '')
        cand.num_challenges_solved = request.POST.get('numChallengesSolved')
        cand.expertise_level = request.POST.get('expertiseLevel')
        cand.data_strs = request.POST.get('dataStrs')
        cand.algos = request.POST.get('algos')
        cand.cplusplus = request.POST.get('cplusplus')
        cand.java = request.POST.get('java')
        cand.python = request.POST.get('python')
        cand.save()
        return HttpResponse("Added candidate successfully")
    return HttpResponse("Authorization denied")


def delete_cand(request):
    if request.POST.get('authcode') == settings.ADMIN_AUTH_CODE:
        Candidate.objects.filter(name=requ.POST.get('name')).delete()
        return HttpResponse("Removed candidate successfully")
    return HttpResponse("Authorization denied")
