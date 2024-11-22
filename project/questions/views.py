from django.shortcuts import render,redirect
from django.utils import timezone
from questions.models import Question

# Create your views here.
def question_detail(request, question_id):
  question = Question.objects.get(id=question_id)
  context = {'question' : question} # 딕셔너리
  return render(request,'question_detail.html',context)

# 목록을 띄워주는 함수
def question_list(request):
  keyword=request.GET.get('keyword','')
  questions = Question.objects.filter(subject__icontains=keyword)|Question.objects.filter(content__icontains=keyword)
  context = {'questions' : questions, 'keyword':keyword}
  return render(request, 'question_list.html',context)

# 질문을 생성하는 함수
# Model.odjects.create() 으로 DB에 내용을 저장할 수 있다.
def question_create(request):
  if request.method =='GET':
    return render(request, 'question_create.html')
  elif request.method=='POST':
    question = Question.objects.create(
      subject = request.POST['subject'],
      content=request.POST['content'],
      create_date=timezone.now()
    )
    return redirect('/questions')
  

def question_delete(request,question_id):
    question= Question.objects.get(id=question_id)
    question.delete()
    return redirect('/questions') 
  
def question_update(request, question_id):
  question = Question.objects.get(id = question_id)

  if request.method == 'GET':
    context = {'question':question}
    return render(request, 'question_update.html', context)
  
  if request.method == "POST":
    question.subject = request.POST['subject']
    question.content = request.POST['content']
    question.save()
    return redirect(f'/questions/{question_id}')
