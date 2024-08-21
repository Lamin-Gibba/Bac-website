from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ContactUS,Home,Aboutus,mission_and_vission,Powers_and_Functions,TestiM,chairman,councilmembers,ceo,Staffs_of_Council,Planing_and_Dev,Budget_finance,Rates_and_Taxes
from django.contrib import messages


# Create your views here. 
def Index(request):
    posts = Home.objects.all()
    return render(request, 'index.html',{'posts':posts})

def About(request):
    posts = Aboutus.objects.all()
    return render(request, 'about.html', {'posts':posts})

def Services(request):
    return render(request, 'services.html')

def Contact(request):

    return render(request, 'contact.html')

def Project(request):
    return render(request, 'project.html')

def Testimonial(request):
    posts = TestiM.objects.all()
    return render(request, 'testimonial.html',{'posts':posts})
    
def Sanitation(request):
    return render(request, 'sanitatione.html')

def Education(request):
    return render(request, 'education.html')

def Team(request):
    return render(request, 'team.html')

def Error(request):
    return render(request, '404.html')

def Health(request):
    return render(request, 'health.html')

def Community(request):
    return render(request, 'community.html')

def Agriculture(request):
    return render(request, 'agriculture.html')

def Community(request):
    return render(request, 'community.html')

def Lands(request):
    return render(request, 'lands.html')

def Mission(request):
     posts = mission_and_vission.objects.all()
     return render(request, 'mission&vission.html',{'posts':posts})

def Powersfunctions(request):
     posts = Powers_and_Functions.objects.all()
     return render(request, 'powers&functions.html',{'posts':posts})

def Demographic(request):
    return render(request, 'demographic-map.html')

def Chairman(request):
    posts = chairman.objects.all()
    return render(request, 'chairman.html',{'posts':posts})

def Clerk(request):
    posts =  Staffs_of_Council.objects.all()
    return render(request, 'staffs-of-council.html',{'posts':posts})

def Ceo(request):
    posts = ceo.objects.all()
    return render(request, 'ceo.html',{'posts':posts})

def Planningdevelopment(request):
    posts = Planing_and_Dev.objects.all()
    return render(request, 'planning&development.html',{'posts':posts})

def Council(request):
    posts = councilmembers.objects.all()

    return render(request, 'council-members.html',{'posts':posts})

def Ratestaxes(request):
    posts = Rates_and_Taxes.objects.all()
    return render(request, 'rates&taxes.html',{'posts':posts})

def Budgetfinance(request):
    posts = Budget_finance.objects.all()
    return render(request, 'Budget&finance.html',{'posts':posts})

def Partners(request):
    return render(request, 'partners.html')

def Intpartners(request):
    return render(request, 'int-partners.html')

def Publications(request):
    return render(request, 'publication.html')

def Sanitation(request):
    return render(request, 'sanitation.html')



def sendData(request):
    #data = ContactUS.objects.all()
    #context= {"data":data}
    if request.method == "POST":
     name = request.POST.get('name')
     email = request.POST.get('email')
     subject = request.POST.get('subject')
     message = request.POST.get('message')

     print(name,email,subject,message)
     query = ContactUS(name=name,email=email,subject=subject,message=message)
     query.save()
     messages.info(request,"Quote send successfully Thank You!")

     return render(request, 'contact.html',)






