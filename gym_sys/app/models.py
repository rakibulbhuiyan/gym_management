from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Banners(models.Model):
    img=models.ImageField(upload_to='banners/')
    alt_text=models.CharField(max_length=150)
    class Meta:
        verbose_name_plural='Banners'
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
    validate_time=models.IntegerField(null=True)    
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
    regis_date=models.DateTimeField(auto_now_add=True,null=True)

@receiver(post_save,sender=User)
def create_subcriber(sender,instance,created,**kwargs):
    if created:
        Subscriber.objects.create(user=instance)
class Trainer(models.Model):
    full_name=models.CharField(max_length=150)
    username=models.CharField(max_length=150,null=True)
    password=models.CharField(max_length=50,null=True)
    mobile=models.CharField(max_length=150)
    salary=models.IntegerField(default=0)
    address=models.TextField()
    is_active=models.BooleanField(default=False)
    detail=models.TextField()
    img=models.ImageField(upload_to='trainer/',null=True)
    def __str__(self) -> str:
        return str(self.full_name)
    def image_tag(self):
        if self.img:
            return mark_safe('<img src="%s" width="80" />' %(self.img.url)) 
# CSV file Attached here
class TrainerCSV(models.Model):
    trainercsv=models.FileField(upload_to='trainercsv/',null=True)
class Notify(models.Model):
    notify_detail=models.TextField()
    readby_user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    readby_trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE,blank=True,null=True)
    is_read = models.BooleanField(default=False)
    def __str__(self) -> str:
        return str(self.notify_detail) 
# sibscriber --> Trainer 
class AssignSubscriber(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE,blank=True)

    def __str__(self) -> str:
        return str(self.user)
# achivements of Trainer
class TrainerAchivements(models.Model):
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=150)
    detail=models.TextField()
    img=models.ImageField(upload_to='achivements/',null=True)
    class Meta:
        verbose_name_plural='TrainerAchivements'
    def __str__(self) -> str:
        return str(self.title)
    def image_tag(self):
        if self.img:
            return mark_safe('<img src="%s" width="80" />' %(self.img.url)) 
        else:
            return 'No image'

#Trainer Salary include
class Trainersalary(models.Model):
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    amount=models.IntegerField()
    amount_date=models.DateField()
    remarks=models.TextField(blank=True)
    def __str__(self) -> str:
        return str(self.trainer.full_name)
    class Meta:
        verbose_name_plural='Trainer Salary'
# Trainer Notifications.....
class TrainerNotifications(models.Model):
    notif_msg = models.TextField()
    def __str__(self) -> str:
        return self.notif_msg
    class Meta:
        verbose_name_plural='Trainer Notifications'
# create notifTrainer status for create relationship...
class NotifTrainerStatus(models.Model):
    notif=models.ForeignKey(TrainerNotifications,on_delete=models.CASCADE)
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    class Meta:
        verbose_name_plural='Trainer Notification Status'
# subscriber message model 
class Trainermsg(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE,null=True)
    message = models.TextField()

    class Meta:
        verbose_name_plural='Message for Trainer'