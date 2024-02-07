from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import UpdateView,DeleteView,CreateView
from category.models import Category

from .models import Category
from .forms import CategoryForm
def category_list(request):
    categorys = Category.objects.all()
    context = {'category_list':categorys}
    return render(request, 'category/index.html',context)

def addForm(request):
    form=CategoryForm()
    context={'category':form}
    if request.method == 'POST':
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            Category.objects.create(name=request.POST['name'])
            
            r=reverse("category_list")
            return HttpResponseRedirect(r)
       
        else:
            context['msg']='category not vaild'
    return render(request, 'category/addcategory.html',context)

def category_delete(request,id):
    
        Category.objects.filter(id=id).delete()
        r=reverse("category_list")
        return HttpResponseRedirect(r)
# Generic View
class category_update(UpdateView):
     model=Category
     template_name='category/update.html'
    #  context_object_name='form'
     form_class=CategoryForm
     success_url=reverse_lazy('category_list')

class categorydeleted(DeleteView):
      model = Category
      template_name = 'category/delete.html'
      success_url = reverse_lazy('category_list')  
    
class category_Create(CreateView):
    model = Category
    template_name = 'category/update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')     

