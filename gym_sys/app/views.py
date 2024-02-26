from django.shortcuts import render,redirect
from .models import (Banners,Service,Pages,Faq,Gallery,GalleryImage,SubcripPlan,SubcripPlanFeature,Trainer,
                     Notify,Subscription,AssignSubscriber,Trainersalary,TrainerNotifications,Trainermsg
                     )
from django.core import serializers
from django.http import JsonResponse
from .forms import (EnquiryForm,SignupForm,ProfileForm,TrainerLoginForm,TrainerProfileForm,TrainerPasswordForm)
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from datetime import timedelta
# Create your views here.
def home(request):
    banners=Banners.objects.all()
    services=Service.objects.all()
    gal_Img=GalleryImage.objects.all().order_by('-id')[:9]
    context={
        'banners':banners,
        'services':services,
        'gal_Img':gal_Img,
    }
    return render(request, 'home.html',context)

def page_detail(request,id):
    pages=Pages.objects.get(id=id)
    context={
        'pages':pages,
    }
    return render(request, 'page.html',context)

def faq_list(request):
    faqs=Faq.objects.all()
    context={
        'faqs':faqs,
    }
    return render(request, 'faq.html',context)

def enquiry(request):
    if request.method=='POST':
        form=EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully achieved')
            return redirect('enquiry')
        else:
            messages.error(request,'Invalid Data')
    else:
        form=EnquiryForm()
    context={
        'form':form,
    }
    return render(request, 'enquiry.html',context)

def gellary(request):
    gellary=Gallery.objects.all().order_by('-id')
    context={
        'gellary':gellary,
    }
    return render(request, 'gellary.html',context)

def gellary_detail(request,id):
    gellary=Gallery.objects.get(id=id)
    gellary_images=GalleryImage.objects.filter(gellary=gellary).order_by('-id')
    context={
        'gellary_images':gellary_images, 
        'gellary':gellary, 
    }
    return render(request, 'gellary_detail.html',context)

def pricing(request):
    plans=SubcripPlan.objects.annotate(total_member=Count('subscription__id')).all().order_by('price',)
    dfeatures=SubcripPlanFeature.objects.all()
    context={
        'plans':plans,
        'dfeatures':dfeatures,
    }
    return render(request, 'pricing.html',context)
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully signup')
            return redirect('home')
        else:
            messages.error(request,'Invalid Data')
            return redirect('signup')
    else:
        form=SignupForm()
    context={
        'form':form
    }
    return render(request, 'registration/signup.html',context)
#checkout block
def checkout(request,plan_id):
    plandetail=SubcripPlan.objects.get(pk=plan_id)
    context={
        'plan':plandetail,
    }
    return render(request, 'checkout.html',context)
# User Dashboard
def user_dashboard(request):
    current_plan = None
    my_trainer = None
    total_notifications = None
    endtime = None
    try:
        current_plan = Subscription.objects.get(user=request.user)
        my_trainer = AssignSubscriber.objects.get(user=request.user)
        unread_notifications = Notify.objects.filter(is_read=False).order_by('-id')
        read_notifications = Notify.objects.filter(is_read=True).order_by('-id')
        total_notifications = unread_notifications.union(read_notifications)
        endtime=current_plan.regis_date+timedelta(days=current_plan.plan.validate_time)
    except ObjectDoesNotExist:
        # if subscription does not exist
        current_plan = None
    context = {
        'current_plan': current_plan,
        'my_trainer': my_trainer,
        'total_notifications': total_notifications,
        'endtime': endtime,
    }
    return render(request,'dashboard.html',context)

def update_Profile(request):
    if request.method=='POST':
        form=ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully Updated')
            return redirect('update_profile')
    else:
        form = ProfileForm(instance=request.user)
    context={
        'form':form,
    }
    return render(request,'edit_profile.html',context)
#trainer login info:::
def trainerlogin(request):
    form = TrainerLoginForm()
    if request.method=='POST':
        username=request.POST['username']
        pwd=request.POST['password']
        trainer=Trainer.objects.filter(username=username,password=pwd).count()
        if trainer > 0:
            trainer=Trainer.objects.filter(username=username,password=pwd).first()
            request.session['trainerlogin']=True
            request.session['trainerid']=trainer.id
            return redirect('trainer_dashboard')
        else:
            messages.error(request,'Invalid!!!')
    else:
        form =TrainerLoginForm()
    context={
        'form':form
    }
    return render(request, 'registration/trainerlogin.html',context)
# trainer logout
def trainerlogout(request):
    del request.session['trainerlogin']
    return redirect('trainerlogin')
#   Notificetion
def notification(request):
    unread_notifications = Notify.objects.filter(is_read=False).order_by('-id')
    read_notifications = Notify.objects.filter(is_read=True).order_by('-id')
    total_notifications = unread_notifications.union(read_notifications)
    context = {
        'unread_notifications': unread_notifications,
        'read_notifications': read_notifications,
        'total_notifications': total_notifications,
    }
    return render(request, 'notification.html', context)

def get_notifs(request):
    data=Notify.objects.all().order_by('-id')
    jsonData=serializers.serialize('json',data)
    return JsonResponse({'data':jsonData})

def mark_as_read(request, notification_id):
    if request.method == 'POST':
        notification = Notify.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()
        messages.success(request, 'Notification marked as read.')
    return redirect('notification')


# trainer dashboard (trainer profile,subcription,subcriber)
def trainer_dashboard(request):
    return render(request, 'registration/trainer_dashboard.html')
# trainer bia data
def trainer_profile(request):
    train_id=request.session['trainerid']
    trainer=Trainer.objects.get(id=train_id)
    form=TrainerProfileForm(instance=trainer)
    if request.method=='POST':
        form=TrainerProfileForm(request.POST,request.FILES,instance=trainer)
        if form.is_valid():
            form.save()
            messages.success(request,'profile data updated successfully!!!')
    
    context={
        'form':form
    }
    return render(request, 'registration/trainer_profile.html',context)
# trainer subcriber
def trainer_subcriber(request):
    trainer=Trainer.objects.get(pk=request.session['trainerid'])
    trainer_subcriber=AssignSubscriber.objects.filter(trainer=trainer).order_by('-id')
    context={
        'trainer':trainer,
        'trainer_subcriber':trainer_subcriber,
    }
    return render(request,'registration/trainer_subcriber.html',context)

# trainer payments
def trainer_payments(request):
    trainer=Trainer.objects.get(pk=request.session['trainerid'])
    trainer_pays=Trainersalary.objects.filter(trainer=trainer).order_by('-id')
    context={
        'trainer':trainer,
        'trainer_pays':trainer_pays,
    }
    return render(request,'registration/trainer_payments.html',context)
# password change for trainer
def trainer_password_change(request):
    trainer=Trainer.objects.get(pk=request.session['trainerid'])#use for who is login to logout so session create
    if request.method=='POST':
        new_password=request.POST['new_password']
        updatepass=Trainer.objects.filter(pk=request.session['trainerid']).update(password=new_password)#update password and logout.
        if updatepass:
            del request.session['trainerlogin']
            return redirect('trainerlogin')
        else:
            messages.error(request,'not updated')
    form=TrainerPasswordForm
    return render(request,'registration/trainer_change_pass.html',{'form':form})
# trainer notifications
def trainer_notifs(request):
    data=TrainerNotifications.objects.all().order_by('-id')# get all trainer data by reverse id 
    context={
        'notifs':data,
    }
    return render(request,'registration/trainer_notification.html',context)
#  trainer messages
def trainer_message(request):
    data=Trainermsg.objects.all().order_by('-id')# get all trainer data by reverse id 
    context={
        'msgs':data,
    }
    return render(request,'registration/message.html',context)