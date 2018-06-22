from django.db import models

# Create your models here.
class Interintrnsip_2018(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Phone = models.BigIntegerField()
    CurrentCity = models.CharField(max_length=50)
    Question1 = models.TextField(verbose_name = "Q1. Why should you be hired for this internship?",)
    Question2 = models.TextField(verbose_name = "Q2. Are you available for 1 month, starting immediately, for a full time internship at Delhi? If not, what is the time period you are available for and the earliest date you can start this internship on?")
    Institute = models.CharField(max_length=150,default='', blank=True)
    Degree = models.CharField(max_length=200,default='', blank=True)
    Stream = models.CharField(max_length=100,default='', blank=True)
    Choosed_Department = models.CharField(max_length=50)
    Current_Year_Of_Graduation = models.CharField(max_length=50,null=True,verbose_name = "Current Year Of Graduation")
    Performance_PG = models.CharField(max_length=50,default='',verbose_name = "PG Performance")
    Performance_UG = models.CharField(max_length=50,default='', blank=True,verbose_name = "UG Performance")
    Performance_12 = models.CharField(max_length=50,default='', blank=True,verbose_name = "12 Performance")
    Performance_10 = models.CharField(max_length=50,default='', blank=True,verbose_name = "10 Performance")
    Link_to_application = models.URLField(verbose_name = "Link to application")
    
    DataAnalytics = 'Data Analytics'
    PolicyResearch = 'Policy Research'
    SocialMedia = 'Social Media'
    Legal = 'Legal'
    defult = ' '
    HumanResource = 'Human Resource'
    Deparment_CHOICES = (
        (DataAnalytics, 'Data Analytics'),
        (PolicyResearch, 'Policy Research'),
        (SocialMedia, 'Social Media'),
        (Legal, 'Legal'),
        (HumanResource, 'HumanResource'),
        (defult,'---'),
        )
    Assigned_Department = models.CharField(
        verbose_name = "Assigned Department" ,   
        max_length=2,
        choices=Deparment_CHOICES,
        default=defult,
    )
    
    
    Select = 'Select'
    NotSelect = 'NotSelect'
    Hold = 'Hold'
    defult = ' '
    Statu = (
        (Select, 'Select'),
        (NotSelect, 'Not Select'),
        (Hold, 'Hold'),
        (defult, '---')
    
    )
    Status = models.CharField(
           
        max_length=2,
        choices=Statu,
        default=defult,
    )
    
    Assigned_Username = models.CharField(max_length=50)
    Assigned_Password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Name
    
class FeedBack(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Phone = models.BigIntegerField()
    Department = models.CharField(max_length=50)
    Post = models.CharField(max_length=200)
    Feedback = models.TextField()
    
    Others = models.CharField(max_length=250,default='', blank=True)  
    
    def __str__(self):
        return self.Name
    