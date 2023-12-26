from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
# 
def display_topics(request):

    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    QLWO=Webpage.objects.all().order_by(Length('name')) 
    QLWO=Webpage.objects.filter(topic_name='Cricket').order_by('name')
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(topic_name='Cricket').order_by('name')[1:5]
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket')&Q(url__endswith='in'))
    QLWO=Webpage.objects.all()

    #Webpage.objects.filter(name='chaithu').update(name='Shami')
    Webpage.objects.filter(name='Shami').update(topic_name='FootBall')

    QLWO=Webpage.objects.all()
    #Webpage.objects.filter(topic_name='Cricket').delete()
    QLWO=Webpage.objects.all()

    d={'webpages':QLWO}

    return render(request,'display_webpages.html',d)


"""def delete_webpage(request):
        QLWO=Webpage.objects.all()
        Webpage.objects.filter(topic_name='volleyball').delete()
        QLWO=Webpage.objects.all()
        d={'webpages':QLWO}
        return render(request,'display_webpages.html',d)"""



def display_records(request):
    QLAO=AccessRecord.objects.all()
    #QLAO=AccessRecord.objects.filter(pk_lt=5)
    #QLAO=AccessRecord.objects.filter(name__startswith='r')
    #QLAO=AccessRecord.objects.filter(date__year__in=('2023','1998')

    d={'AccessRecords':QLAO}
    return render(request,'display_records.html',d)


def insert_topic(request):
    tn=input('enter your topic')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_records.html',d)


def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    TO=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    NWO.save()  
    QLWO=Webpage.objects.all()

    d={'webpages':QLWO}
    return render(request,'display_webpages.html',d)


def insert_access(request):
    pk=int(input('enter pk value of object'))
    a=input('enter author')
    d=input("enter date")
    wo=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=wo,author=a,date=d)[0]
    NAO.save()
    QLAO=AccessRecord.objects.all()
    d={'AccessRecords':QLAO}
    return render(request,'display_records.html',d)







