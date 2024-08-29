from django.contrib import admin
from .import models 
# Register your models here.

admin.site.register(models.Aboutus)
admin.site.register(models.Home)
admin.site.register(models.mission_and_vission)
admin.site.register(models.Powers_and_Functions)
admin.site.register(models.TestiM)
admin.site.register(models.chairman)
admin.site.register(models.ContactUS)
admin.site.register(models.councilmembers)
admin.site.register(models.ceo)
admin.site.register(models.Staffs_of_Council)
admin.site.register(models.Planing_and_Dev)
admin.site.register(models.Budget_finance)
admin.site.register(models.Rates_and_Taxes)
admin.site.register(models.projects)
admin.site.register(models.partnerUS)
admin.site.register(models.IntpartnerUS)

class AgricultureAdmin(admin.ModelAdmin):
     list_display=('title','content','featured_image')
admin.site.register(models.Agriculture,AgricultureAdmin)

class CommunityAdmin(admin.ModelAdmin):
     list_display=('title','content','featured_image')
admin.site.register(models.Community,CommunityAdmin)
    
class EducationAdmin(admin.ModelAdmin):
     list_display=('title','content','featured_image')
admin.site.register(models.Education,EducationAdmin)

class FeatureAdmin(admin.ModelAdmin):
     list_display=('title','content','featured_image')
admin.site.register(models.Fearture,FeatureAdmin)

admin.site.register(models.Health)
admin.site.register(models.IntPartner)

class LandAdmin(admin.ModelAdmin):
     list_display=('title','content','featured_image')
admin.site.register(models.Land,LandAdmin)


class PublicationAdmin(admin.ModelAdmin):
     list_display=('title','content','featured_image')
admin.site.register(models.Publication,PublicationAdmin)

class SanitationAdmin(admin.ModelAdmin):
     list_display=('title','content','featured_image')
admin.site.register(models.Sanitation,SanitationAdmin)

class ServicesAdmin(admin.ModelAdmin):
     list_display=('title','content','featured_image')
admin.site.register(models.Services,ServicesAdmin)

class TeamAdmin(admin.ModelAdmin):
     list_display=('title','content','featured_image')
admin.site.register(models.Team,TeamAdmin)



