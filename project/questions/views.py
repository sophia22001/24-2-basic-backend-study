from django.shortcuts import render
from questions.models import Question

# Create your views here.
def question_detail(request, question_id):
  question = Question.objects.get(id=question_id)
  context = {'question' : question} # 딕셔너리
  return render(request,'question_detail.html',context)

# 목록을 띄워주는 함수
def question_list(request):
  questions = Question.objects.all()
  context = {'questions' : questions}
  return render(request, 'question_list.html',context)