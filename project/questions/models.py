from django.db import models

# Create your models here.
# models.py에 클래스를 생성하면, 장고가 클래스를 토대로 DB 테이블을 생성해준다.
class Question(models.Model):
  subject = models.CharField(max_length=200)
  content = models.TextField() # 내용 길이를 예측하기 힘들 때
  create_date = models.DateTimeField()