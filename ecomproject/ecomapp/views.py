from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def index(request):
    return HttpResponse('HELLO ECOM WORLD')

def AllProdCat(request,c_slug=None):
    c_page=None
    prods_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        prods_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        prods_list=Product.objects.all().filter(available=True)
    paginator=Paginator(prods_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        prods_list=paginator.page(page)
    except (EmptyPage,InvalidPage):
        prods_list=paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':c_page,'products':prods_list})

def prodCatDeet(request,c_slug,prod_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=prod_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})