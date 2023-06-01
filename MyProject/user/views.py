from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
        request.session['cart']=ct
    x=category.objects.all().order_by('-id')[0:6]
    pdata=myproduct.objects.all().order_by('-id')[0:7]
    mydict={"data":x,"prodata":pdata}
    return render(request,'user/index.html',context=mydict)
def about(request):
    return render(request,'user/aboutus.html')
##########################################
def product(request):
    return render(request,'user/product.html')
##########################################
def myorder(request):
    return render(request,'user/myorder.html')
##########################################
def enquiry(request):
    status=False
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mob')
        d=request.POST.get('msg')
        contactus(Name=a,Mobile=c,Email=b,Message=d).save()
        status=True

        #mdict={"Name":a,"Email":b,"Mobile":c,"Message":d}

    msg={"m":status}
    return render(request,'user/enquiry.html',context=msg)
##########################################
def signup(request):
    if request.method=="POST":
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Mobile=request.POST.get('mob')
        Passwd=request.POST.get('passwd')
        Address=request.POST.get('address')
        Picture=request.POST.get('pic')
        x=register.objects.all().filter(email=Email).count()
        if x==0:
            register(name=Name,email=Email,mobile=Mobile,ppic=Picture,passwd=Passwd,address=Address).save()
            return HttpResponse("<script>alert('You are registered successfuly');location.href='/user/signup/'</script>")
        else:
            return HttpResponse("<script>alert('Your email id is registered....' );location.href='/user/signup/'</script>")
    return render(request,'user/signup.html')
    ##########################################
def myprofile(request):
    return render(request,'user/myprofile.html')
#########################################

def signin(request):
    if request.method=="POST":
        Email=request.POST.get('email')
        Passwd=request.POST.get('passwd')
        x=register.objects.all().filter(email=Email,passwd=Passwd).count()
        if x==1:
            request.session['userid']=Email
            return HttpResponse("<script>alert('You logged in successfully..');location.href='/user/signin/'</script>")
        else:
            return HttpResponse("<script>alert('Your userid or password in incorrect');location.href='/user/signin /'</script>")
    return render(request,'user/signin.html')


###########################################
def Novel(request):
    cid=request.GET.get('msg')
    cat=category.objects.all().order_by('-id')
    d=myproduct.objects.all().filter(mcategory=1)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=1,pcategory=cid)
    mydict={"cats":cat,"data":d,"a":cid}
    return render(request,'user/Novel.html',mydict)
###########################################
def Fictional(request):
    cid = request.GET.get('msg')
    cat = category.objects.all().order_by('-id')
    d = myproduct.objects.all().filter(mcategory=2)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=2, pcategory=cid)
    mydict = {"cats": cat, "data": d, "a": cid}
    return render(request,'user/Fictional.html',mydict)
############################################
def Academic(request):
    cid = request.GET.get('msg')
    cat = category.objects.all().order_by('-id')
    d = myproduct.objects.all().filter(mcategory=3)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=3, pcategory=cid)
    mydict = {"cats": cat, "data": d, "a": cid}
    return render(request,'user/Academic.html',mydict)

def viewproduct(request):
    a = request.GET.get('abc')
    x = myproduct.objects.all().filter(id=a)
    return render(request, 'user/viewproduct.html', {"pdata": x})

############################################################## ############

def signout(request):
    if request.session.get('userid'):
        del request.session['userid']
    return HttpResponse("<script>alert('You are signed out...');location.href='/user/index/'</script>")


####################################################################################3
def myordr(request):
    user=request.session.get('userid')
    pid=request.GET.get('msg')
    if user:
        if pid is not None:
            morder(userid=user,pid=pid,remarks="Pending",odate=datetime.now().date(),status=True).save
            return HttpResponse("<script>alert('Your order is confirmed...');location.href='/user/index/'</script>")
    else:
        return HttpResponse("<script>alert('You have to login first...');location.href='/user/signin/'</script>")
    return render(request)

def mycart(request):
    p=request.GET.get('pid')
    user=request.session.get('userid')
    if user:
        if p is not None:
            mycart(userid=user,pid=p,cdate=datetime.now().date,status=True).save()
            return HttpResponse("<script>alert('Your item is added to cart...');location.href='/user/index/'</script>")
    else:
        return HttpResponse("<script>alert('YOu have to login first..');location.href='/user/signin/'</script>")
    return render(request,'user/mcart.html')












