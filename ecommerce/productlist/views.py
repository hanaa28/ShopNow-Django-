from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
products = [{
    'id': 1,
    'price': '20$',
    'path': '0.jpg',
    'category':'jeans'
},
{
    'id': 2,
    'price': '30$',
    'path': '1.jpg',
    'category':'jeans'
},
{
    'id': 3,
    'price': '40$',
    'path': '2.jpg',
    'category':'jeans'
},
{
    'id': 4,
    'price': '20$',
    'path': '3.jpg',
    'category':'jeans'
},
{
    'id': 5,
    'price': '30$',
    'path': 's3.jpg',
    'category':'suit'
},
{
    'id': 6,
    'price': '40$',
    'path': 'b3.jpg',
    'category':'jeans'
},
{
    'id': 7,
    'price': '20$',
    'path': 'b5.jpg',
    'category':'jeans'
},
{
    'id': 8,
    'price': '30$',
    'path': 'b6.jpg',
    'category':'jeans'
},
{
    'id': 9,
    'price': '40$',
    'path': 's1.jpg',
    'category':'jeans'
}]

from .models import Product

def product_list(request):
    products = Product.objects.all()
    context = {'product_list': products}
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
        
        # name = request.POST.get('pname')
        # description = request.POST.get('pdescription')
        # price = request.POST.get('pprice')
        
       
        Product.objects.create(name=request.POST['pname'], description=request.POST['pdescription'], price=request.POST['pprice'])
        
        r=reverse("product_list")
        return HttpResponseRedirect(r)
        # return HttpResponseRedirect('/')  
    return render(request, 'productlist/AddProduct.html')
def product_delete(request,id):
    
        Product.objects.filter(id=id).delete()
        r=reverse("product_list")
        return HttpResponseRedirect(r)
    