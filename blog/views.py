from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from .forms import BlogForms
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    blogs = Blog.objects
    context = {"b_o":blogs}
    return render(request,'index.html', context)

@login_required
def new(request):
    if request.method == 'POST':
        forms = BlogForms(request.POST)

        if forms.is_valid:
            forms.save()
            return redirect('index')
    forms = BlogForms()
    return render(request,'new.html',{'forms':forms})

def detail(request,blog_id):
    blog_one=get_object_or_404(Blog,id=blog_id)
    context={'blog_one':blog_one}
    return render(request,'detail.html',context)

@login_required
def edit(request,blog_id):
    blog_edit=get_object_or_404(Blog,id=blog_id)
    if request.method == 'POST':
        forms = BlogForms(request.POST,instance=blog_edit)
        if forms.is_valid:
            forms.save()
            return redirect('index')
        
    forms = BlogForms(instance=blog_edit)
    return render(request,'new.html',{'forms':forms})

@login_required
def delete(request,blog_id):
    blog_delete=get_object_or_404(Blog,id=blog_id)
    blog_delete.delete()
    return redirect('index')
