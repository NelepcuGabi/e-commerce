from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout 
from django.shortcuts import render,redirect
from item.models import Category,Item
from .forms import SignupForm
# Create your views here
def home(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()

    return render(request,'core/home.html',{
                  'categories':categories,
                  'items':items,
        })

def contact(request):
    return render(request,'core/contact.html')


def about(request):
    return render(request,'core/about.html')

def signup(request):
    form = SignupForm()
    if request.method =='POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
        
        else:
            form = SignupForm()


    
    return render(request,'core/signup.html',{
        'form':form
    })
@login_required
def logout_view(request):
    auth_logout(request)

    return redirect('core:home')