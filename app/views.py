from django.shortcuts import render

def jinjatag(request):
    d={'a':int(input('enter ur value of a - ')),'b':int(input('enter ur value of b - ')),'c':int(input('enter ur value of c - ')),'f':int(input('enter ur value of f - '))}
    return render(request,'jinja.html',d)
