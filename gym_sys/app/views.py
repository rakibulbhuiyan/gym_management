from django.shortcuts import render,redirect
from .models import Banners,Service,Pages,Faq,Gallery,GalleryImage,SubcripPlan,SubcripPlanFeature
from .forms import EnquiryForm,SignupForm,ProfileForm
from django.contrib import messages

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
    plans=SubcripPlan.objects.all().order_by('id',)
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

def user_dashboard(request):
    return render(request,'dashboard.html')

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