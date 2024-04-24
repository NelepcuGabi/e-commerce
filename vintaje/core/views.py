from django.shortcuts import render
from item.models import Category,Item
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

