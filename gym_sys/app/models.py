from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Banners(models.Model):
    img=models.ImageField(upload_to='banners/')
    alt_text=models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.alt_text
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' %(self.img.url))
class Service(models.Model):
    title=models.CharField(max_length=150)
    detail=models.TextField()
    img=models.ImageField(upload_to='services/')

    def __str__(self) -> str:
        return self.title
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' %(self.img.url))
class Pages(models.Model):
    title=models.CharField(max_length=150)
    detail=models.TextField()

    def __str__(self) -> str:
        return self.title
class Faq(models.Model):
    ques=models.TextField()
    ans=models.TextField()
    
    def __str__(self) -> str:
        return self.ques
    # enter you data
class Enquiry(models.Model):
    full_name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    detail=models.TextField()
    send_time=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.full_name

class Gallery(models.Model):
    title=models.CharField(max_length=150)
    img=models.ImageField(upload_to='gellary/',null=True)
    detail=models.TextField()
    def __str__(self) -> str:
        return self.title
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' %(self.img.url))
# All gellary Image show by this model
class GalleryImage(models.Model):
    gellary=models.ForeignKey(Gallery,on_delete=models.CASCADE, null=True)
    alt_text=models.CharField(max_length=150)
    img=models.ImageField(upload_to='gellary_images/',null=True)
    def __str__(self) -> str:
        return self.alt_text
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' %(self.img.url))

#subcription plan::::::::
class SubcripPlan(models.Model):
    title=models.CharField(max_length=150)    
    price=models.IntegerField()    
    max_member=models.IntegerField(null=True)    
    highlight_status=models.BooleanField(default=False,null=True)
    def __str__(self) -> str:
        return self.title

#subcription Feature asigned
class SubcripPlanFeature(models.Model):
    # subcripplan=models.ForeignKey(SubcripPlan,on_delete=models.CASCADE)   
    subcripplan=models.ManyToManyField(SubcripPlan)   
    title=models.CharField(max_length=150)     
    def __str__(self) -> str:
        return self.title 
# here creating amount 
class PlanDiscount(models.Model):
    subcripplan=models.ForeignKey(SubcripPlan,on_delete=models.CASCADE,null=True)
    total_month=models.IntegerField()
    total_discount=models.IntegerField()
    def __str__(self) -> str:
        return str(self.total_month)
# subcribe model
class Subscriber(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile=models.CharField(max_length=20)
    address=models.TextField()
    img=models.ImageField(upload_to='subscriber/',null=True)
    def __str__(self) -> str:
        return str(self.user)
    def image_tag(self):
        if self.img:
            return mark_safe('<img src="%s" width="80" />' %(self.img.url)) 
        else:
            return 'No Image'
# create subcription here
class Subscription(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    plan=models.ForeignKey(SubcripPlan,on_delete=models.CASCADE,null=True)
    price=models.CharField(max_length=50)

@receiver(post_save,sender=User)
def create_subcriber(sender,instance,created,**kwargs):
    if created:
        Subscriber.objects.create(user=instance)