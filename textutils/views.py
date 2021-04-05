# i have created this file - kunanj
from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
    #file = open("1.txt", 'r+')
    #return HttpResponse(file.read())

    #return HttpResponse("<h1>Navigation Bar </h1><br>"
                     #   " <a href='https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7'> "
                     #   "Django Playlist </a> <br>"
                     #   "<a href='https://www.codewithharry.com/videos/python-django-tutorials-hindi-6'>"
                      #  "code with harry</a> <br>"
                       # "<a href='https://www.technicians.dev'>technicians.dev</a>")

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home "
    #                     "<a href='http://127.0.0.1:8000/removepunc'> removepunc </a>"
    #                     "<a href='http://127.0.0.1:8000/capitalizefirst'> capitalize first </a>"
    #                     "<a href='http://127.0.0.1:8000/spaceremove'> space remove </a>"
    #                     "<a href='http://127.0.0.1:8000/newlineremove'> new line remove </a>"
    #                     "<a href='http://127.0.0.1:8000/charcount'> char count </a>")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # chechk checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    allcaps = request.POST.get('allcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    # print(removepunc)
    # print(djtext)

    # check which check box is on
    if removepunc == 'on':

        # analyzed_text = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'remove punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', params)

    if (allcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'All Upper case', 'analyzed_text': analyzed}
        djtext = analyzed



    if(spaceremover == 'on'):
        analyzed = " "
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose':'Sapce Remover', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', params)

    if(charcounter == 'on'):
        analyzed = " "
        count = 0
        for char in djtext:
            if not(char == " "):
                analyzed = analyzed + char
                count = count + 1

        params = {'purpose':'char counter', 'analyzed_text': count}
        djtext = analyzed

    if (newlineremover == 'on'):
        analyzed = " "
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")

        # print("pre", analyzed)
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}


    if(charcounter != 'on' and spaceremover != 'on' and newlineremover != 'on' and allcaps != 'on' and removepunc != 'on'):
        return HttpResponse("Please choose an option")
    # else:
    #     return HttpResponse("Error")

    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("capitalize First "
#                         "<a href='/'>back</a>")