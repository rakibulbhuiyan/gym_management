from django.db import models
from django.utils.html import mark_safe

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

class GalleryImage(models.Model):
    gellary=models.ForeignKey(Gallery,on_delete=models.CASCADE, null=True)
    alt_text=models.CharField(max_length=150)
    img=models.ImageField(upload_to='gellary_images/',null=True)
    def __str__(self) -> str:
        return self.alt_text
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' %(self.img.url))