from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from books.models import Book
# Create your views here.

def home(request):
    context={'name':'Anto','age':21}
    return render(request,'home.html',context)

@login_required
def add_books(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        pa=request.POST['pa']
        l=request.POST['l']

        c=request.FILES['i']
        f=request.FILES['f']

        b=Book.objects.create(title=t,author=a,price=p,pages=pa,language=l,cover=c,pdf=f)
        b.save()     #saves the record inside table
        return redirect('books:view')
    return render(request,'add.html')

@login_required
def view_books(request):
    k=Book.objects.all()        #Reads all records from table Book assigns it to k
    context={'Book':k}
    return render(request,'view.html',context)

@login_required
def detail(request,p):
    k=Book.objects.get(id=p)
    return render(request,'detail.html',{'book':k})

@login_required
def edit(request,p):
    k=Book.objects.get(id=p)
    if(request.method=="POST"):
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.price=request.POST['p']
        k.pages=request.POST['pa']
        k.language=request.POST['l']
        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.cover=request.FILES.get('i')
        if(request.FILES.get('f')==None):
            k.save()
        else:
            k.pdf=request.FILES.get('f')
        k.save()
        return view_books(request)
    return render(request,'edit.html',{'book':k})

@login_required
def delete(request,p):
    k=Book.objects.get(id=p)
    k.delete()
    return redirect('books:view')

from django.db.models import Q
def searchbooks(request):
    k=None  #initalizes k as None
    if(request.method=="POST"):
        query=request.POST['q'] #get the input key from form
        if query:
            k=Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))   #it checks the key in title and author field of every records.
            #filter function records only the matching records.

    return render(request,'search.html',{'Book':k})