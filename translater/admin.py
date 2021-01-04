from django.contrib import admin

from .models import Word, WordFromUser

admin.site.register(Word)
admin.site.register(WordFromUser)
