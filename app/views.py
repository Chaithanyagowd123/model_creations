from django.shortcuts import render
from app.models import *
# Create your views here.
# 
def display_topics(request):

    QLTO=Topic.objects.all()
    d={'topics':QLTO}


    return render(request,'display_topics.html',d)



def display_webpages(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}

    return render(request,'display_webpages.html',d)


def display_records(request):
    QLAO=AccessRecord.objects.all()
    d={'AccessRecords':QLAO}

    return render(request,'display_records.html',d)