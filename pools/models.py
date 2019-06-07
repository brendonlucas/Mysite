from django.db import models


class Questions(models.Model):
    question_text = models.CharField(max_length=255)
    closed = models.BooleanField(default=False)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice_text


"""
from pools.models import *
q1 = Questions(question_text='Qual o certo?')
q2 = Questions(question_text='Escolha um animal?')
q3 = Questions(question_text='Escolha uma cor?')

id = Questions.objects.get(id=1)
c1 = Choice(question=id, choice_text='Bolacha', votes=0).save()
c2 = Choice(question=id, choice_text='Biscoito', votes=0).save()

id = Questions.objects.get(id=2)
c3 = Choice(question=id, choice_text='Gato', votes=0).save()
c4 = Choice(question=id, choice_text='Coelho', votes=0).save()
c5 = Choice(question=id, choice_text='Cachorro', votes=0).save()

id = Questions.objects.get(id=3)
c6 = Choice(question=id, choice_text='Preto', votes=0).save()
c7 = Choice(question=id, choice_text='Azul', votes=0).save()
c8 = Choice(question=id, choice_text='Amarelo', votes=0).save()
"""


