from django.db import models
from django.contrib.auth import  get_user_model
# Create your models here.
user=get_user_model()
#작성
class Post(models.Model):
    image=models.ImageField(verbose_name='img')
    content=models.TextField(verbose_name='내용')
    createdat=models.DateTimeField(verbose_name='작성일',auto_now_add=True)
    viewcount=models.IntegerField(verbose_name='조회수')
    writer=models.ForeignKey(to=user,on_delete=models.CASCADE,null=True,blank=True)
    # django-admin startproject config.
# django-admin startapp posts
# python manage.py makemigrations 테이블을 만들기
# python manage.py migrate 실제 데이터베이스 생성
# python manage.py createsuperuser 가상유저 생성
#데이터베이스를 연결하는 방법
#댓글
class comment(models.Model):
    content=models.TextField(verbose_name='내용')
    createdat=models.DateTimeField(verbose_name='작성일')
    post=models.ForeignKey(to='post',on_delete=models.CASCADE)
    writer=models.ForeignKey(to=user,on_delete=models.CASCADE,null=True,blank=True)
