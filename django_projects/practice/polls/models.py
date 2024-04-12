import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# 모델 생성
# 모델을 테이블에 써 주기 위한 마이그레이션을 만듬
# 이 모델에 맞는 테이블을 만듬

class Question(models.Model):
    question = models.CharField(max_length=200, verbose_name='질문')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    owner = models.ForeignKey('auth.User', related_name='questions', on_delete=models.CASCADE, null=True)

    @admin.display(boolean=True, description='최근생성(하루기준)')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        if self.was_published_recently():
            new_badge = 'NEW!'
        else:
            new_badge = ''
        return "{} 제목: {}, 날짜: {}".format(new_badge, self.question, self.pub_date)

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return "[{}] {}".format(self.question.question, self.choice_text)

class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)

    # Vote 인스턴스에는 한개의 question과 한개의 voter만 생성하도록 제약조건 걸어ㅇ
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question', 'voter'], name='unique_voter_for_questions')
        ]