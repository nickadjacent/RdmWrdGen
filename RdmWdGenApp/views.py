from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import random
import string


def index(request):
    return render(request, "index.html")


def random_word(request):
    if 'count' not in request.session:
        request.session['count'] = 0
        unique_id = ''
    else:
        request.session['count'] += 1
        allowed_chars = ''.join((string.ascii_letters, string.digits))
        unique_id = ''.join(random.choice(allowed_chars) for _ in range(14))
        print(unique_id)
    context = {
        'word': unique_id
    }
    return render(request, "index.html", context)


def reset(request):
    request.session.clear()
    return redirect('/random_word')
