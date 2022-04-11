# I have created this file- Pranav

from ast import Param
from glob import escape
from string import punctuation
from tkinter import Place
from urllib import request
from django.http import  HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    #chek Checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off') 
    extraspaceremover = request.POST.get(' extraspaceremover', 'off')
    charactercount = request.POST.get('charactercount', 'off') 

    if (removepunc == "on"):

        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': "Removed Punctuations",  'analyzed_text': analyzed}
        djtext = analyzed
    #Analyze the Text

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper case',  'analyzed_text': analyzed}
        djtext = analyzed

    #Analyze the Tex
    
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': ' Extra Space Remover',  'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines',  'analyzed_text': analyzed}
        djtext = analyzed

    elif(charactercount=="on"):
        analyzed = ""
        for char in djtext:
            if char!=" ":
                analyzed = analyzed + char
            else:
                continue
            char_len = len(analyzed)
        params = {'purpose': 'Character Counts',  'analyzed_text': char_len}

    if(removepunc != "on" and fullcaps != "on" and extraspaceremover !="on"  and newlineremover !="on" and charactercount !="on" ) :
        return HttpResponse ("Please select any operation and Try Again!")

    return render(request, 'Analyze.html', params)


