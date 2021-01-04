from django.db import models

class Word(models.Model):
    ru = models.CharField('Русский', max_length=50)
    en = models.CharField('Английский', max_length=50)

    def __str__(self):
        return self.en

class WordFromUser(models.Model):
    user_word = models.CharField('Слово', max_length=50)

    def __str__(self):
        return self.user_word
