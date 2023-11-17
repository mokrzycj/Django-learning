import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# Model reprezentujący pytanie w bazie danych
class Question(models.Model):
    # Pole przechowujące tekst pytania o maksymalnej długości 200 znaków
    question_text = models.CharField(max_length=200)
    
    # Pole przechowujące datę publikacji pytania
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

# Model reprezentujący odpowiedź w bazie danych
class Choice(models.Model):
    # Pole przechowujące informację o pytaniu, z którym jest powiązane, 
    # ponadto przez zastosowanie ForeignKey, jeśli powiązazne z odpowiedziami pytanie zostanie usunięte
    # to samo stanie się z odpowiedziami
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    # Pole przechowujące tekst opcji odpowiedzi o maksymalnej długości 200 znaków
    choice_text = models.CharField(max_length=200)
    
    # Pole przechowujące liczbę głosów dla danej odpowiedzi, z domyślną wartością 0
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
