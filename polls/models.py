from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Aboutus(models.Model):
         image_about = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         content_stra_plan = models.TextField(blank=True,null=True)
         strplan1 = models.TextField(blank=True,null=True)
         strplan2 = models.TextField(blank=True,null=True)
         strplan3 = models.TextField(blank=True,null=True)
         strplan4 = models.TextField(blank=True,null=True)
         strplan5 = models.TextField(blank=True,null=True)
         telephone_CallUs = models.CharField(max_length=50,blank=True, null=True)
         constituencies = models.IntegerField(blank=True,null=True)
         wards = models.IntegerField(blank=True,null=True)
         villages = models.IntegerField(blank=True,null=True)
         Councillors = models.FloatField(max_length=50, blank=True, null=True)
         vission = models.TextField(blank=True,null=True)
         mission = models.TextField(blank=True,null=True)
         Title_name_chairman = models.CharField(max_length=200, blank=True, null=True)
         image_chairm = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_vice = models.CharField(max_length=200, blank=True, null=True)
         image_vice = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_ceo = models.CharField(max_length=200, blank=True, null=True)
         image_ceo = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_finance = models.CharField(max_length=200, blank=True, null=True)
         image_finace = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_service = models.CharField(max_length=200, blank=True, null=True)
         image_service = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_planning = models.CharField(max_length=200, blank=True, null=True)
         image_planning = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         unity = models.TextField(blank=True,null=True)

class Home(models.Model):
         bg_image_sli1 = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True) 
         bg_image_sli2 = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)         
         bg_image_sli3 = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         bg_image_sli4 = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)         
         
         desc_BAC = models.CharField(max_length=200, blank=True, null=True)
         content_BAC = models.TextField(blank=True,null=True)
         image_BAC = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         content_Local_Tailored = models.TextField(blank=True,null=True)
         telephone_reach_out = models.CharField(max_length=50, blank=True, null=True)

         image_about_BAC = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Description_headqut = models.CharField(max_length=200, blank=True, null=True)
         content_about_BAC = models.TextField(blank=True,null=True)
         Aerial_space = models.FloatField(max_length=30, blank=True, null=True)
         telephone_CallUs = models.CharField(max_length=50,blank=True, null=True)
         
         Jurisdic_of_Council = models.TextField(blank=True,null=True)
         Road_Ntw_Infras = models.TextField(blank=True,null=True)
         quote_Ntw_infras = models.CharField(max_length=200, blank=True,null=True)
         Public_and_Enviro_Health = models.TextField(blank=True,null=True)
         quote_enviro_health = models.CharField(max_length=200, blank=True,null=True)
         Natural_Resoures = models.TextField(blank=True,null=True)
         quote_Nat_Resourse = models.CharField(max_length=200, blank=True,null=True)

         aerial_space = models.FloatField(max_length=30, blank=True, null=True)
         Pop_density = models.FloatField(max_length=30, blank=True, null=True)
         Population = models.FloatField(max_length=30, blank=True, null=True)
         Yearly_Pop_shift = models.FloatField(max_length=30, blank=True, null=True)

         Title_name_chairman = models.CharField(max_length=200, blank=True, null=True)
         Description_chairm = models.CharField(max_length=200, blank=True, null=True)
         title_image_chairm = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         Title_name_vice = models.CharField(max_length=200, blank=True, null=True)
         Description_vice = models.CharField(max_length=200, blank=True, null=True)
         title_image_vice = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         Title_name_ceo = models.CharField(max_length=200, blank=True, null=True)
         Descriptio_ceo = models.CharField(max_length=200, blank=True, null=True)
         title_image_ceo = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         Testim_name_teacher = models.CharField(max_length=200, blank=True, null=True)
         words_teach = models.TextField(blank=True,null=True)
         Description_teacher = models.CharField(max_length=200, blank=True, null=True)
         testim_image_teacher = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         Testim_nurs = models.CharField(max_length=200, blank=True, null=True)
         words_nurs = models.TextField(blank=True,null=True)
         Description_nurs = models.CharField(max_length=200, blank=True, null=True)
         testim_image_nurs = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         Testim_busim = models.CharField(max_length=200, blank=True, null=True)
         words_busim = models.TextField(blank=True,null=True)
         Description_busim = models.CharField(max_length=200, blank=True, null=True)
         testim_image_busim = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

class Budget_finance(models.Model):
         bg_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)         
         mandate_para = models.TextField(blank=True,null=True)
         image_finas = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         content_p1 = models.TextField(blank=True,null=True)
         content_p2 = models.TextField(blank=True,null=True)
         content_p3 = models.TextField(blank=True,null=True)
         content_p4 = models.TextField(blank=True,null=True)
         content_p5 = models.TextField(blank=True,null=True)
         content_p6 = models.TextField(blank=True,null=True)
         content_p7 = models.TextField(blank=True,null=True)
         content_p8 = models.TextField(blank=True,null=True)
         content_p9 = models.TextField(blank=True,null=True)
         content_p10 = models.TextField(blank=True,null=True)
         content_p11 = models.TextField(blank=True,null=True)
         content_p12 = models.TextField(blank=True,null=True)

class sanitation(models.Model):
         sani_para = models.TextField(blank=True,null=True)
         bg_image_sani = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)         
         Desc_tips = models.TextField(blank=True,null=True)
         Sub_Desc_tips = models.TextField(blank=True,null=True)
         Tips1 = models.TextField(blank=True,null=True)
         Tips2 = models.TextField(blank=True,null=True)
         Tips3 = models.TextField(blank=True,null=True)

class education(models.Model):
         educat_para = models.TextField(blank=True,null=True)
         bg_image_educat = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)         
         Desc_tips = models.TextField(blank=True,null=True)
         Sub_Desc_tips = models.TextField(blank=True,null=True)
         Tips1 = models.TextField(blank=True,null=True)
         Tips2 = models.TextField(blank=True,null=True)
         Tips3 = models.TextField(blank=True,null=True)
         
class health(models.Model):
         hlth_para = models.TextField(blank=True,null=True)
         bg_image_hlth = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)         
         Desc_tips = models.TextField(blank=True,null=True)
         Sub_Desc_tips = models.TextField(blank=True,null=True)
         Tips1 = models.TextField(blank=True,null=True)
         Tips2 = models.TextField(blank=True,null=True)
         Tips3 = models.TextField(blank=True,null=True)

class agriculture(models.Model):
         agric_para = models.TextField(blank=True,null=True)
         bg_image_agric = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)         
         Desc_tips = models.TextField(blank=True,null=True)
         Sub_Desc_tips = models.TextField(blank=True,null=True)
         Tips1 = models.TextField(blank=True,null=True)
         Tips2 = models.TextField(blank=True,null=True)
         Tips3 = models.TextField(blank=True,null=True)

class community(models.Model):
         comu_para = models.TextField(blank=True,null=True)
         bg_image_comu = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)         
         Desc_tips = models.TextField(blank=True,null=True)
         Sub_Desc_tips = models.TextField(blank=True,null=True)
         Tips1 = models.TextField(blank=True,null=True)
         Tips2 = models.TextField(blank=True,null=True)
         Tips3 = models.TextField(blank=True,null=True)

class land(models.Model):
         land_para = models.TextField(blank=True,null=True)
         bg_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)         
         Desc_tips = models.TextField(blank=True,null=True)
         Sub_Desc_tips = models.TextField(blank=True,null=True)
         Tips1 = models.TextField(blank=True,null=True)
         Tips2 = models.TextField(blank=True,null=True)
         Tips3 = models.TextField(blank=True,null=True)
   
class ceo(models.Model):
         bg_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)         
         mandate_para = models.TextField(blank=True,null=True)
         image_ceo = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         content_p1 = models.TextField(blank=True,null=True)
         content_p2 = models.TextField(blank=True,null=True)
         content_p3 = models.TextField(blank=True,null=True)
         content_p4 = models.TextField(blank=True,null=True)
         content_p5 = models.TextField(blank=True,null=True)
         content_p6 = models.TextField(blank=True,null=True)
         content_p7 = models.TextField(blank=True,null=True)
         content_p8 = models.TextField(blank=True,null=True)
         content_p9 = models.TextField(blank=True,null=True)
         content_p10 = models.TextField(blank=True,null=True)
         content_p11 = models.TextField(blank=True,null=True)
         content_p12 = models.TextField(blank=True,null=True)
         content_p13 = models.TextField(blank=True,null=True)

class chairman(models.Model):
         bg_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)         
         mandate_para = models.TextField(blank=True,null=True)
         image_chaim = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         content_p1 = models.TextField(blank=True,null=True)
         content_p2 = models.TextField(blank=True,null=True)
         content_p3 = models.TextField(blank=True,null=True)
         content_p4 = models.TextField(blank=True,null=True)
         content_p5 = models.TextField(blank=True,null=True)
         content_p6 = models.TextField(blank=True,null=True)
         content_p7 = models.TextField(blank=True,null=True)
         content_p8 = models.TextField(blank=True,null=True)
         content_p9 = models.TextField(blank=True,null=True)
         content_p10 = models.TextField(blank=True,null=True)
         content_p11 = models.TextField(blank=True,null=True)
         content_p12 = models.TextField(blank=True,null=True)
         content_p13 = models.TextField(blank=True,null=True)

class ContactUS(models.Model):
         
         name = models.CharField(max_length=50, blank=True, null=True)
         #Last_Name = models.CharField(max_length=50, null=True)
         email = models.EmailField()
         message = models.TextField()
         subject = models.CharField(max_length=100,blank=True, null=True)
         #Created_Date = models.DateField(auto_now_add=True)

class partnerUS(models.Model):
         name = models.CharField(max_length=50, blank=True, null=True)
         #Last_Name = models.CharField(max_length=50, null=True)
         email = models.EmailField()
         phone = models.IntegerField()
         organization = models.CharField(max_length=100,blank=True, null=True)
         select = models.SlugField(blank=True, null=True)
         message = models.TextField()
         #Created_Date = models.DateField(auto_now_add=True)

class IntpartnerUS(models.Model):
         name = models.CharField(max_length=50, blank=True, null=True)
         #Last_Name = models.CharField(max_length=50, null=True)
         email = models.EmailField()
         phone = models.IntegerField()
         organization = models.CharField(max_length=100,blank=True, null=True)
         select = models.SlugField(blank=True, null=True)
         message = models.TextField()
         #Created_Date = models.DateField(auto_now_add=True)


class Staffs_of_Council(models.Model):
         bg_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)         
         name_chair = models.CharField(max_length=200, blank=True, null=True)
         title_image_chair = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_chair = models.CharField(max_length=200,null=True)

         name_vchair = models.CharField(max_length=200, blank=True, null=True)
         title_image_Vchair = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_vchair = models.CharField(max_length=200,null=True)
   
         name_commun = models.CharField(max_length=200, blank=True, null=True)
         title_image_commun = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_commun = models.CharField(max_length=200,null=True)

         name_plan = models.CharField(max_length=200, blank=True, null=True)
         title_image_plan = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_plan = models.CharField(max_length=200,null=True)

         name_finas = models.CharField(max_length=200, blank=True, null=True)
         title_image_finas = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_finas = models.CharField(max_length=200,null=True)

         name_yp = models.CharField(max_length=200, blank=True, null=True)
         title_image_yp = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_yp = models.CharField(max_length=200,null=True)

         name_bget = models.CharField(max_length=200, blank=True, null=True)
         title_image_bget = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_bget = models.CharField(max_length=200,null=True)

         name_IT = models.CharField(max_length=200, blank=True, null=True)
         title_image_IT = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_IT = models.CharField(max_length=200,null=True)

         name_sec = models.CharField(max_length=200, blank=True, null=True)
         title_image_sec= models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_sec = models.CharField(max_length=200,null=True)

         name_sen_RVC = models.CharField(max_length=200, blank=True, null=True)
         title_image_RVC = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_RVC = models.CharField(max_length=200,null=True)

         name_ass_acc = models.CharField(max_length=200, blank=True, null=True)
         title_image_acc = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_acc = models.CharField(max_length=200,null=True)

         name_plumb = models.CharField(max_length=200, blank=True, null=True)
         title_image_plumb = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_plumb = models.CharField(max_length=200,null=True)

         name_assAcc= models.CharField(max_length=200, blank=True, null=True)
         title_image_assAcc = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_assAcc = models.CharField(max_length=200,null=True)

         name_plann= models.CharField(max_length=200, blank=True, null=True)
         title_image_plann = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_plannn = models.CharField(max_length=200,null=True)

         name_ratesM= models.CharField(max_length=200, blank=True, null=True)
         title_image_ratesM = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_ratesM = models.CharField(max_length=200,null=True)

         name_mason= models.CharField(max_length=200, blank=True, null=True)
         title_image_mason = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_mason = models.CharField(max_length=200, blank=True,null=True)

class projects(models.Model):
         bag_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         Date_and_year1 = models.CharField(blank=True,null=True)
         Desc1 = models.CharField(blank=True,null=True)
         Sub_desc1 = models.CharField(blank=True,null=True)
         content1  = models.TextField(blank=True,null=True)
 
         Date_and_year2 = models.CharField(max_length=200,blank=True,null=True)
         Desc2 = models.CharField(blank=True,null=True)
         Sub_desc2 = models.CharField(blank=True,null=True)
         content2  = models.TextField(blank=True,null=True)

         Date_and_year3 = models.CharField(max_length=200,blank=True,null=True)
         Desc3 = models.CharField(blank=True,null=True)
         Sub_desc3 = models.CharField(blank=True,null=True)
         content3  = models.TextField(blank=True,null=True)

         Date_and_year4 = models.CharField(max_length=200,blank=True,null=True)
         Desc4 = models.CharField(blank=True,null=True)
         Sub_desc4 = models.CharField(blank=True,null=True)
         content4  = models.TextField(blank=True,null=True)

         Date_and_year5 = models.CharField(blank=True,null=True)
         Desc5 = models.CharField(blank=True,null=True)
         Sub_desc5 = models.CharField(blank=True,null=True)
         content5  = models.TextField(blank=True,null=True)

         Date_and_year6 = models.CharField(max_length=200,blank=True,null=True)
         Desc6 = models.CharField(blank=True,null=True)
         Sub_desc6 = models.CharField(blank=True,null=True)
         content6  = models.TextField(blank=True,null=True)

         content_price  = models.TextField(blank=True,null=True)

      
class mission_and_vission(models.Model):
         bg_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         vission = models.TextField(blank=True,null=True)
         mission = models.TextField(blank=True,null=True)
         legal_mandate = models.TextField(blank=True,null=True)
         image_mis_vis = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

class Planing_and_Dev(models.Model):
         bg_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)         
         mandate_para = models.TextField(blank=True,null=True)
         image_plan = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         content_p1 = models.TextField(blank=True,null=True)
         content_p2 = models.TextField(blank=True,null=True)
         content_p3 = models.TextField(blank=True,null=True)
         content_p4 = models.TextField(blank=True,null=True)
         content_p5 = models.TextField(blank=True,null=True)
         content_p6 = models.TextField(blank=True,null=True)
         content_p7 = models.TextField(blank=True,null=True)
         content_p8 = models.TextField(blank=True,null=True)
         content_p9 = models.TextField(blank=True,null=True)
         content_p10 = models.TextField(blank=True,null=True)
         content_p11 = models.TextField(blank=True,null=True)
         content_p12 = models.TextField(blank=True,null=True)
         content_p13 = models.TextField(blank=True,null=True)

        

class Powers_and_Functions (models.Model):
         bg_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         powers_sct48_li1 = models.CharField(max_length=300, blank=True,null=True)
         powers_sct48_li2 = models.CharField(max_length=300, blank=True,null=True)
         powers_sct48_li3 = models.CharField(max_length=300, blank=True,null=True)
         powers_sct48_li4 = models.CharField(max_length=300, blank=True,null=True)
         powers_sct48_li5 = models.CharField(max_length=300, blank=True,null=True)
         powers_sct48_li6 = models.CharField(max_length=300, blank=True,null=True)
         powers_sct48_li7 = models.CharField(max_length=300, blank=True,null=True)

         legis_pow_li1 = models.CharField(max_length=300, blank=True,null=True)
         legis_pow_li2 = models.CharField(max_length=300, blank=True,null=True)

         miscel_pow_li1 = models.CharField(max_length=300, blank=True,null=True)
         miscel_pow_li2 = models.CharField(max_length=300, blank=True,null=True)
         miscel_pow_li3 = models.CharField(max_length=300, blank=True,null=True)
         miscel_pow_li4 = models.CharField(max_length=300, blank=True,null=True)

         image_functions = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         functions_of_BAC = models.TextField(blank=True,null=True)

         education_li1 = models.TextField(blank=True,null=True)
         education_li2 = models.TextField(blank=True,null=True)
         education_li3 = models.TextField(blank=True,null=True)
         education_li4 = models.TextField(blank=True,null=True)
         education_li5 = models.TextField(blank=True,null=True)
         education_li6 = models.TextField(blank=True,null=True)
         education_li7 = models.TextField(blank=True,null=True)
         education_li8 = models.TextField(blank=True,null=True)
         education_li9 = models.TextField(blank=True,null=True)
         education_li10 = models.TextField(blank=True,null=True)
         education_li11 = models.TextField(blank=True,null=True)

         image_other_powers = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         other_powers = models.TextField(blank=True,null=True)
         other_powers_li1 = models.TextField(blank=True,null=True)
         other_powers_li2 = models.TextField(blank=True,null=True)
         other_powers_li3 = models.TextField(blank=True,null=True)
         other_powers_li4 = models.TextField(blank=True,null=True)

         criti_legal_policy_para1 = models.TextField(blank=True,null=True)
         Desc_cri_leg_para2 = models.TextField(blank=True,null=True)
         criti_li1 = models.CharField(max_length=300,blank=True,null=True)
         criti_li2 = models.CharField(max_length=300,blank=True,null=True)
         criti_li3 = models.CharField(max_length=300,blank=True,null=True)
         criti_li4 = models.CharField(max_length=300,blank=True,null=True)
         criti_li5 = models.CharField(max_length=300,blank=True,null=True)
         criti_li6 = models.CharField(max_length=300,blank=True,null=True)
         criti_li7 = models.CharField(max_length=300,blank=True,null=True)
         criti_li8 = models.CharField(max_length=300,blank=True,null=True)
         criti_li9 = models.CharField(max_length=300,blank=True,null=True)
         criti_li10 = models.CharField(max_length=300,blank=True,null=True)
         criti_li11 = models.CharField(max_length=300,blank=True,null=True)
         criti_li12 = models.CharField(max_length=300,blank=True,null=True)
         criti_li13 = models.CharField(max_length=300,blank=True,null=True)
         criti_li14 = models.CharField(max_length=300,blank=True,null=True)
         criti_li15 = models.CharField(max_length=300,blank=True,null=True)
         criti_li16 = models.CharField(max_length=300,blank=True,null=True)
         criti_li17 = models.CharField(max_length=300,blank=True,null=True)
         criti_li18 = models.CharField(max_length=300,blank=True,null=True)
         criti_li19 = models.CharField(max_length=300,blank=True,null=True)
         criti_li20 = models.CharField(max_length=300,blank=True,null=True)

         

class Publication(models.Model):
         title = models.CharField(max_length=200,null=True)
         content = models.TextField(max_length=500,blank=True,null=True)
         featured_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

class IntPartner(models.Model):
         title = models.CharField(max_length=200,null=True)
         content = models.TextField(max_length=500,blank=True,null=True)
         featured_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

class Rates_and_Taxes(models.Model):
         pRates = models.TextField(blank=True,null=True)
         bRates = models.TextField(blank=True,null=True)
         sRates = models.TextField(blank=True,null=True)
         R_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         blicense = models.TextField(blank=True,null=True)
         permit = models.TextField(blank=True,null=True)
         license_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         OperatMarkets = models.TextField(blank=True,null=True)
         RegulatMarkets = models.TextField(blank=True,null=True)
         markets_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         RegulatFines = models.TextField(blank=True,null=True)
         traffic_fines = models.TextField(blank=True,null=True)
         fines_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         Debts_managem = models.TextField(blank=True,null=True)
         F_planin = models.TextField(blank=True,null=True)
         debts_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         Land_Use = models.TextField(blank=True,null=True)
         Land_Regulations = models.TextField(blank=True,null=True)
         Land_Management = models.TextField(blank=True,null=True)
         Land_Transfer = models.TextField(blank=True,null=True)
         conflick_Resolution = models.TextField(blank=True,null=True)
         Land_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
   

class councilmembers (models.Model):
         bg_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         name_chair = models.CharField(max_length=200, blank=True, null=True)
         title_image_chair = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Title_name_chair = models.CharField(max_length=200,null=True)

         name_vchair = models.CharField(max_length=200, blank=True, null=True)
         title_image_Vchair = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         ward_vchair = models.CharField(max_length=200,null=True)
   
         name3 = models.CharField(max_length=200, blank=True, null=True)
         image3 = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         ward3 = models.CharField(max_length=200,null=True)

         name4 = models.CharField(max_length=200, blank=True, null=True)
         image4 = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         ward4 = models.CharField(max_length=200,null=True)

         name5 = models.CharField(max_length=200, blank=True, null=True)
         image5 = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         ward5 = models.CharField(max_length=200,null=True)

         name6 = models.CharField(max_length=200, blank=True, null=True)
         image6 = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         ward6 = models.CharField(max_length=200,null=True)

         name7 = models.CharField(max_length=200, blank=True, null=True)
         image7 = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         ward7 = models.CharField(max_length=200,null=True)

         name8 = models.CharField(max_length=200, blank=True, null=True)
         image8 = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         ward8 = models.CharField(max_length=200,null=True)

         name9 = models.CharField(max_length=200, blank=True, null=True)
         image9 = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         ward9 = models.CharField(max_length=200,null=True)

         name10 = models.CharField(max_length=200, blank=True, null=True)
         image10 = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         ward10 = models.CharField(max_length=200,null=True)

         name11 = models.CharField(max_length=200, blank=True, null=True)
         image11 = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         ward11 = models.CharField(max_length=200,null=True)

         name12 = models.CharField(max_length=200, blank=True, null=True)
         image12 = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         ward12 = models.CharField(max_length=200,null=True)

        
class Team(models.Model):
         title = models.CharField(max_length=200,null=True)
         content = models.TextField(max_length=500,blank=True,null=True)
         featured_image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

        

class testimonial(models.Model):
         image_words_pple = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
         Testim_name_teacher = models.CharField(max_length=200, blank=True, null=True)
         words_teach = models.TextField(blank=True,null=True)
         Description_teacher = models.CharField(max_length=200, blank=True, null=True)
         testim_image_teacher = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         Testim_nurs = models.CharField(max_length=200, blank=True, null=True)
         words_nurs = models.TextField(blank=True,null=True)
         Description_nurs = models.CharField(max_length=200, blank=True, null=True)
         testim_image_nurs = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         Testim_busim = models.CharField(max_length=200, blank=True, null=True)
         words_busim = models.TextField(blank=True,null=True)
         Description_busim = models.CharField(max_length=200, blank=True, null=True)
         testim_image_busim = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)

         banna_para1 = models.TextField(blank=True,null=True)
         



