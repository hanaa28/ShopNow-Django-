from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from category.models import Category

# to this import statement
from .models import Category

from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    context = {'product_list': products}
    print(products[0].get_image_url())
    return render(request, 'productlist/index.html', context)

def product_detail(request,id):
    # filtered_products = filter(lambda item: item['id'] == id, products)
    # product_item = list(filtered_products)
    filter_products = Product.objects.get(id=id)
    context = {'product_item': filter_products}
    if context:
      return render(request, 'productlist/product_detail.html',context)
    else:
        return render(request,'productlist/NotFound.html')

def product_add(request):
    if request.method == 'POST':
        Product.objects.create(name=request.POST['pname'], 
                               description=request.POST['pdescription'],
                            price=request.POST['pprice'],
                            image=request.FILES['pimage'],
                           )
        
        r=reverse("product_list")
        return HttpResponseRedirect(r)
        # return HttpResponseRedirect('/')  
    return render(request, 'productlist/AddProduct.html')

def addForm(request):
    form=ProductForm()
    
    if request.method == 'POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            Product.objects.create(name=request.POST['name'], 
                                description=request.POST['description'],
                                price=request.POST['price'],
                                image=request.FILES['image'],
                                 category=Category.objects.get(id=request.POST['category']))
            
            r=reverse("product_list")
            return HttpResponseRedirect(r)
            return HttpResponseRedirect('/')  
        else:
            context['msg']='Product not vaild'

    context = {'product': form}
    
    return render(request, 'productlist/AddProductForm.html',context)


def product_delete(request,id):
    
        Product.objects.filter(id=id).delete()
        r=reverse("product_list")
        return HttpResponseRedirect(r)


def product_update(request,id):
    products=Product.objects.get(id=id)
    context={"products": products}
    if request.method == 'POST':
            if request.POST['pname'] != '' and request.POST['pdescription'] != '' and request.POST['pprice'] != '':
                products.name = request.POST['pname']
                products.description = request.POST['pdescription']
                products.price = request.POST['pprice']
                
                # Check if a new image is uploaded
                if 'pimage' in request.FILES:
                    products.image = request.FILES['pimage']
                
                products.save()
                return HttpResponseRedirect(reverse("product_list"))
            else:
                 context['msg']="fill all feilds"
    
    return render(request, 'productlist/product_update.html', context)
