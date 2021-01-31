from django.shortcuts import render,HttpResponse
from portfolio.models import Contact,Project,Personal_info

# Create your views here.

def home(request):
    projects=Project.objects.all()
    return render(request,'index.html',{'project':projects})

def about(request):
    resume=Personal_info.objects.all()
    print(resume[0])
    return render(request,'about.html',{'resume':resume[0]})

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        desc=request.POST['desc']
        #print(name,subject,email,desc,phone)
        ins=Contact(name=name,email=email,phone=phone,subject=subject,desc=desc)
        ins.save()

    return render(request,'contact.html')

def work(request):
    projects=Project.objects.all()
    return render(request,'work.html',{'project':projects})

def project(request,myid):
    p=Project.objects.filter(id=myid)
    return render(request,'work01.html',{'project':p[0]})

