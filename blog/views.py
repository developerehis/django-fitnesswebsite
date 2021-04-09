from django.shortcuts import render, redirect, get_object_or_404
from .models import blog
from .forms import CommentForm
from django.urls import reverse


# Create your views here.
def all_blogs(request):
    blog_list = blog.objects.all()
    context = {
        'blog_list' :blog_list
    }
    return render(request, 'all_blogs.html', context)

def blog_detail(request, id):
    Blog = get_object_or_404(blog, id=id)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.Blog = Blog
            form.save()
            return redirect (reverse('blog.blog_detail', kwargs={
                'id':blog.id
            }))
    context = {
        'Blog':Blog,
        'form':form,

    }
    return render(request, 'blog_detail.html', context)