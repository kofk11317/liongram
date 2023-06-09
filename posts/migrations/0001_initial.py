# Generated by Django 4.2.1 on 2023-05-22 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='img')),
                ('content', models.TextField(verbose_name='내용')),
                ('createdat', models.DateTimeField(verbose_name='작성일')),
                ('viewcount', models.IntegerField(verbose_name='조회수')),
            ],
        ),
    ]
# django-admin startproject config.
# django-admin startapp posts
# python manage.py makemigrations 테이블을 만들기
# python manage.py migrate 실제 데이터베이스 생성