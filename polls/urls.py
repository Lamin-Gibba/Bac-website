from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from. import views


urlpatterns = [
    path('', views.Index,name='Index'),
    path('About_page/about', views.About,name='About'),
    path('contact', views.Contact,name='Contact'),
    path('About_page/mission&vission', views.Mission,name='Mission'),
    path('About_page/powers&functions', views.Powersfunctions,name='Powersfunctions'),
    path('Latest_News/project', views.Project,name='Project'),
    path('team', views.Team,name='Team'),
    path('About_page/testimonial', views.Testimonial,name='Testimonial'),
    path('Services/services', views.Services,name='Services'),
    path('About_page/demographic-map', views.Demographic,name='Demographic'),
    path('The_Council/chairman', views.Chairman,name='Chairman'),
    path('The_Council/staffs-of-council', views.Clerk,name='Clerk'),
    path('The_Council/ceo', views.Ceo,name='Ceo'),
    path('The_Council/council', views.Council,name='Council'),
    path('The_Council/planning&development', views.Planningdevelopment,name='Planningdevelopment'),
    path('The_Council/council-members', views.Council,name='Council'),
    path('The_Council/budget&finance', views.Budgetfinance,name='Budgetfinance'),
    path('Services/lands', views.Lands,name='Lands'),
    path('Services/sanitation', views.Sanitation,name='Sanitation'),
    path('Services/education', views.Education,name='Education'),
    path('Services/health', views.Health,name='Health'),
    path('Services/community', views.Community,name='Community'),
    path('Services/agriculture', views.Agriculture,name='Agriculture'),
    path('publication', views.Publications,name='Publications'),
    path('Partners/partners', views.Partners,name='Partners'),
    path('Partners/int-partners', views.Intpartners,name='Intpartners'),
    path('rates&taxes', views.Ratestaxes,name='Ratestaxes'),
    
    path('send', views.sendData,name='sendData'),
    path('infor', views.sendinfor,name='sendinfor'),
    path('intPart', views.sendpartners,name='sendpartners'),

    ]
#urlpatterns += static(settings.MEDIA.URL, document_root=settings.MEDIA_ROOT) # type: ignore
#urlpatterns += static(settings.STATIC.URL, document_root=settings.STATIC_ROOT) # type: ignore
