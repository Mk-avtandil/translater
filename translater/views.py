from django.shortcuts import render, redirect
from .models import Word, WordFromUser
from .forms import InputForm, SendWords

def check_word(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        form2 = SendWords(request.POST)
        if form.is_valid():
            form.save()
        if form2.is_valid():
            form2.save()
            return redirect('index')
    form = InputForm()
    form2 = SendWords()
    word_from_user = WordFromUser.objects.order_by('-id')[:1]
    temp = ""
    for i in word_from_user:
        temp = i
    word_from_server = Word.objects.filter(en=temp)

    context = {'form': form,'form2': form2, 'word_from_server': word_from_server, 'word_from_user': word_from_user}
    return render(request, 'translater/index.html', context)