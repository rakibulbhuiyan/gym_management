from django.shortcuts import render,redirect
from .models import Banners,Service,Pages,Faq,Enquiry
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



