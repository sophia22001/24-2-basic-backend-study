from django.db import models

# Create your models here.
class Question(models.Model):
  subject = models.CharField(max_length=200)
  content = models.TextField() # 내용 길이를 예측하기 힘들 때
  created_date = models.DateTimeField()