from django.contrib import admin
from .import models 
# Register your models here.

admin.site.register(models.Aboutus)
admin.site.register(models.Home)
admin.site.register(models.mission_and_vission)
admin.site.register(models.Powers_and_Functions)
admin.site.register(models.testimonial)
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
admin.site.register(models.sanitation)
admin.site.register(models.education)
admin.site.register(models.health)
admin.site.register(models.agriculture)
admin.site.register(models.community)
admin.site.register(models.land)   



class PublicationAdmin(admin.ModelAdmin):
     list_display=('title','content','featured_image')
admin.site.register(models.Publication,PublicationAdmin)


class TeamAdmin(admin.ModelAdmin):
     list_display=('title','content','featured_image')
admin.site.register(models.Team,TeamAdmin)

admin.site.register(models.IntPartner)

