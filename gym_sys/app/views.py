from django.shortcuts import render,redirect
from .models import Banners,Service,Pages,Faq,Gallery,GalleryImage
from .forms import EnquiryForm
from django.contrib import messages
# Create your views here.
def home(request):
    banners=Banners.objects.all()
    services=Service.objects.all()
    context={
        'banners':banners,
        'services':services,
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
