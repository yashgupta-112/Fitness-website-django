from django.shortcuts import render
from .models import Contact,Blogpost,Client
# Create your views here.
def home(request):
    return render(request, 'transform/index.html')
def plan(request):
    return render(request, 'transform/plan.html')    
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request, 'transform/contact.html')    
def bmr(request):
    return render(request, 'transform/bmr.html')    
def Register(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        age = request.POST.get('age', '')
        transformation = request.POST.get('transformation', '')
        plan = request.POST.get('plan', '')
        gender = request.POST.get('gender', '')
        Context = Client(name=name,email=email,age=age,phone=phone,transformation=transformation,plan=plan,gender=gender)
        Context.save()


    return render(request, 'transform/contact2.html')  
def blog(request):
    post = Blogpost.objects.all()
    print(post)
    return render(request, 'transform/blog.html',{'post':post})      
