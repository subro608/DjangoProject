from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.
# def products_create_view(request):
#     form = RawProductForm(request.POST or None)
#     if form.is_valid():
#         print(form.cleaned_data)
#         Product.objects.create(**form.cleaned_data)
#     else:
#         print(form.errors)
#     #     form.save()
        
    
#     context = {
#         'form':form   
#     }
#     return render(request, "product/product_create.html", context)
def products_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    
    context = {
        'form':form   
    }
    return render(request, "product/product_create.html", context)
def products_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title':obj.title,
    #     'description':obj.description
    # }
    context = {
        'object':obj    
    }
    return render(request, "product/product_detail.html", context)


def render_intiial_data(request):
    intial_data = {
        'title': "this is my title",
    }
    form = ProductForm(request.POST or None, initial=intial_data)
    if form.is_valid():
        print(form.cleaned_data)
        Product.objects.create(**form.cleaned_data)
    else:
        print(form.errors)
    context = {
        'form':form
    }
    return render(request, "product/product_create.html", context)

def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id) Version1
    obj = get_object_or_404(Product, id=id) #Version2
    context = {
        'object':obj
    }
    return render(request, "product/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("../../")
    context = {
        'object':obj
    }
    return render(request, "product/product_delete.html", context)

def product_list(request):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset
    }
    return render(request, "product/product_list.html", context)