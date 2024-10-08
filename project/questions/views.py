from django.shortcuts import render

# Create your views here.
def index(request):
  name="Kim"
  context={'name':name} # 딕셔너리
  return render(request,'index.html',context)