from django.shortcuts import render
from app.models import *
# Create your views here.
from django.db.models.functions import Length
from django.db.models import Q
def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='Cricket')
    #LOW=Webpage.objects.get(topic_name='Chess')
    LOW=Webpage.objects.exclude(topic_name='Cricket')
    LOW=Webpage.objects.all()[1:2:]
    LOW=Webpage.objects.all().order_by('name')
    LOW=Webpage.objects.all().order_by('-name')
    
    LOW=Webpage.objects.all().order_by(Length('name'))
    #LOW=Webpage.objects.all().
    LOW=Webpage.objects.all().order_by(Length('name').desc())
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__startswith='k')
    LOW=Webpage.objects.filter(email__endswith='.com')
    LOW=Webpage.objects.filter(name__contains='S')
    LOW=Webpage.objects.filter(name__in=('ashu','yAsh'))
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{7}')
    LOW=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name='dhoni'))
    LOW=Webpage.objects.filter(Q(topic_name='Cricket'))
    d={'webpages':LOW}
    return render(request,'display_webpages.html',d)


def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2022-10-10')
    LOA=AccessRecord.objects.filter(date__gte='2022-10-10')
    LOA=AccessRecord.objects.filter(date__lt='2022-10-10')
    LOA=AccessRecord.objects.filter(date__lte='2022-10-10')
    LOA=AccessRecord.objects.filter(date__year='2023')
    LOA=AccessRecord.objects.filter(date__month='10')
    LOA=AccessRecord.objects.filter(date__day='5')
    LOA=AccessRecord.objects.filter(date__year__gt='2023')
    LOA=AccessRecord.objects.filter(date__month__lt='10')
    
    d={'access':LOA}
    return render(request,'display_access.html',d)









