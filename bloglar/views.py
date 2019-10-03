from django.shortcuts import get_object_or_404, render
from .models import Blog

def blog(request):
    bloglar = Blog.objects.all()
    kisa_icerik = []
   
    for blog_element in bloglar:
        ch = 0
        str1 = ""
        for x in range(0,260):
            str1  = str1 + blog_element.icerik[x]
        kisa_icerik.append(str1)
        ch = ch + 1
    mylist = zip(bloglar, kisa_icerik)
    context = {
        'bloglar' : bloglar,
        'mylist' : mylist,
    }
    return render(request, 'bloglar/bloglar.html', context)

def blog_ayrintili(request, blog_id):
    blog1 = get_object_or_404(Blog, pk= blog_id)

    context = {
        'blog1': blog1,
    }
    return render(request, 'bloglar/blog_ozel.html', context)