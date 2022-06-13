from django.db import models

# Create your models here.

class Book(models.Model):
  title=models.CharField(max_length=50)
  author=models.CharField(max_length=50)

  def __str__(self) -> str: # タイトルを返してあげることで~~~ object(1)ではなくタイトルを表示させることができる
    return self.title