from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Candidate, VotedIP
import datetime
from django.conf import settings


def edit_cand(request):
    if request.POST.get('authcode') == settings.CANDIDATE_AUTH_CODE:
        cname = request.POST.get('name')
        cand = Candidate.objects.filter(name__contains=cname)
        cand = cand[0]
        if request.POST.get('numChallengesSolved'):
            cand.num_challenges_solved = request.POST.get('numChallengesSolved')
        if request.POST.get('expertiseLevel'):
            cand.expertise_level = request.POST.get('expertiseLevel')
        if request.POST.get('dataStrs'):
            cand.data_strs = request.POST.get('dataStrs')
        if request.POST.get('algos'):
            cand.algos = request.POST.get('algos')
        if request.POST.get('cplusplus'):
            cand.cplusplus = request.POST.get('cplusplus')
        if request.POST.get('java'):
            cand.java = request.POST.get('java')
        if request.POST.get('python'):
            cand.python = request.POST.get('python')
        cand.save()
        return HttpResponse("Edited details successfully")
    return HttpResponse("Authorization denied")
