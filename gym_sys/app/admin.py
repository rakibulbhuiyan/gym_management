from django.contrib import admin
from .models import Banners,Service,Pages,Faq,Enquiry
# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text','image_tag')
admin.site.register(Banners,BannerAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Service,ServiceAdmin)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Pages,PagesAdmin)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('ques',)
admin.site.register(Faq,FaqAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','detail','send_time')
admin.site.register(Enquiry,EnquiryAdmin)