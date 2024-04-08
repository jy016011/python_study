import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# 모델 생성
# 모델을 테이블에 써 주기 위한 마이그레이션을 만듬
# 이 모델에 맞는 테이블을 만듬

class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now()- datetime.timedelta(days=1)

    def __str__(self):
        if self.was_published_recently():
            new_badge = 'NEW!'
        else:
            new_badge = ''
        return "{} 제목: {}, 날짜: {}".format(new_badge, self.question, self.pub_date)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return "[{}] {}".format(self.question.question, self.choice_text)