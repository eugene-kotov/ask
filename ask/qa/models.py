# coding=utf-8
from django.db import models

#User model
from django.contrib.auth.models import User

#Question model
#u title - заголовок вопроса
#text - полный текст вопроса
#added_at - дата добавления вопроса
#rating - рейтинг вопроса (число)
#author - автор вопроса
#likes - список пользователей, поставивших "лайк"
class Question(models.Model):
    class Meta:
        db_table = 'questions'    
    title    = models.CharField(max_length = 255)
    text     = models.TextField()
    added_at = models.DateTimeField(auto_now = True)
    ratting  = models.IntegerField(default = 0)
    author   = models.ForeignKey(User)
    likes    = models.ManyToManyField(User)
    
    def __str__(self):
        return self.title 
    


#Answer model
#text - текст ответа
#added_at - дата добавления ответа
#question - вопрос, к которому относится ответ
#author - автор ответа
class Answer(models.Model):
    class Meta:
        db_table = 'answers'
    text     = models.TextField()
    added_at = models.DateTimeField(auto_now = True)
    question = models.ForeignKey(Question)
    author   = models.ForeignKey(User)
        
    def __str__(self):
        return self.title 