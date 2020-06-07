from django.shortcuts import render
import random


def home(request):
    return render(request, 'passgen/home.html', {"home": home})


def passwords(request):
    characters = list("abcdefghijklmnopqrst")

    if request.GET.get("Uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("Numbers"):
        characters.extend(str(1234567890))
    if request.GET.get("Special"):
        characters.extend(list(r".,/,',,;,<>?!"))

    length = int(request.GET.get("length"))
    generated = ""

    for i in range(length):
        generated += random.choice(characters)
    return render(request, 'passgen/passwords.html', {"password": generated})
