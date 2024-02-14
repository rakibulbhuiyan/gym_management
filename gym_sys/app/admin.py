from django.contrib import admin
from .models import (Banners,Service,Pages,Faq,Enquiry,Gallery,GalleryImage,
                     SubcripPlan,SubcripPlanFeature,PlanDiscount,Subscriber,Subscription,Trainer,
                     Notify,AssignSubscriber,TrainerAchivements,Trainersalary
                     )
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
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Gallery,GalleryAdmin)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text','image_tag')
admin.site.register(GalleryImage,GalleryImageAdmin)
class SubcripPlanAdmin(admin.ModelAdmin):
    list_editable=('max_member','validate_time','highlight_status')
    list_display = ('title','price','max_member','validate_time','highlight_status')
admin.site.register(SubcripPlan,SubcripPlanAdmin)
class SubcripPlanFeatureAdmin(admin.ModelAdmin):
    list_display=('title','subplans')
    def subplans(self,obj):
        return '|'.join([sub.title for sub in obj.subcripplan.all()])
admin.site.register(SubcripPlanFeature,SubcripPlanFeatureAdmin)

class PlanDiscountAdmin(admin.ModelAdmin):
    list_display=('subcripplan','total_month','total_discount')
admin.site.register(PlanDiscount,PlanDiscountAdmin)
class SubscriberAdmin(admin.ModelAdmin):
    list_display=('user','image_tag','mobile')
admin.site.register(Subscriber,SubscriberAdmin)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display=('user','plan','regis_date','price')
admin.site.register(Subscription,SubscriptionAdmin)
class TrainerAdmin(admin.ModelAdmin):
    list_editable=('is_active',)
    list_display=('full_name','mobile','salary','is_active','image_tag')
admin.site.register(Trainer,TrainerAdmin)
class NotifyAdmin(admin.ModelAdmin):
    list_display=('notify_detail','readby_user','readby_trainer')
admin.site.register(Notify,NotifyAdmin)
class AssignSubscriberAdmin(admin.ModelAdmin):
    list_display=('user','trainer')
admin.site.register(AssignSubscriber,AssignSubscriberAdmin)
class TrainerAchivementsAdmin(admin.ModelAdmin):
    list_display=('trainer','title','image_tag')
admin.site.register(TrainerAchivements,TrainerAchivementsAdmin)
class TrainersalaryAdmin(admin.ModelAdmin):
    list_display=('trainer','amount','amount_date','remarks')
admin.site.register(Trainersalary,TrainersalaryAdmin)