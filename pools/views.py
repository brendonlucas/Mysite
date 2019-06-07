from django.shortcuts import render
from pools.models import *


def index(request):
    return render(request, 'index.html', {'questoes': Questions.objects.order_by('-pub_date').all()})


def question(request, question_id):
    questao = Questions.objects.get(id=question_id)
    return render(request, 'question.html', {'question': questao, 'escolhas': Choice.objects.all()})
