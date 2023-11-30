from django.shortcuts import render, redirect
from .models import Comment, Lista
from .forms import ListaForm, CommentForm
import requests


def comment_list(request):
    comments = Comment.objects.all()
    post_text_dict = {}

    for comment in comments:
        if comment.post in post_text_dict:
            post_text_dict[comment.post].append(comment)
        else:
            post_text_dict[comment.post] = [comment]

    if request.method == 'POST':
        form = ListaForm(request.POST)
        forms = CommentForm(request.POST)
        if form.is_valid() or forms.is_valid():
            if form.is_valid():
                form.save()
            if forms.is_valid():
                forms.save()
            return redirect('')
        # Obsługa usuwania komentarza
        comment_id = request.POST.get('comment_id')
        if comment_id:
            Comment.objects.filter(id=comment_id).delete()
            return redirect('')
    else:
        form = ListaForm()
        forms = CommentForm()

    api_key = '0f973712c93faf52ffbba689370b7df3'
    city = 'Wrocław'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        a = f'Temperature: {round(temp - 273.15,1)} ℃'
        b = f'Description: {desc}'
    else:
        a = 'error'
        b = 'error'

    return render(request, 'home.html', {'post_text_dict': post_text_dict, 'form': form, 'forms': forms, 'a': a, 'b': b})

def delete_all(request):
    Lista.objects.all().delete()
    Comment.objects.all().delete()
    return redirect('')

def con(request):
    return render(request, 'confetti.html')
