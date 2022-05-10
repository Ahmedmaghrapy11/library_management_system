from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import BookForm, CategoryForm

# Create your views here.

# home page function
def index(request):

    if request.method == "POST":
        addedBook = BookForm(request.POST, request.FILES)
        if addedBook.is_valid():
            addedBook.save()
        addedCategory = CategoryForm(request.POST)
        if addedCategory.is_valid():
            addedCategory.save()
    
    context = {
        "categories": Category.objects.all(),
        "books": Book.objects.all(),
        "form": BookForm(),
        "catform": CategoryForm(),
        "allbooks": Book.objects.filter(active= True).count(),
        "booksold": Book.objects.filter(status= "sold").count(),
        "bookrented": Book.objects.filter(status= "rented").count(),
        "bookavailable": Book.objects.filter(status= "available").count(),
    }
    
    return render(request, 'pages/index.html', context)

# book return function
def books(request):

    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains = title)

    context = {
        "categories": Category.objects.all(),
        "books": search,
        "catform": CategoryForm(),
    }

    return render(request, 'pages/books.html', context)

# book update function
def update(request, id):
    
    bookById = Book.objects.get(id=id)
    
    if request.method == "POST":
        updatedBook = BookForm(request.POST, request.FILES, instance=bookById)
        if updatedBook.is_valid():
            updatedBook.save()
            return redirect('/')
    
    else:
        updatedBook = BookForm(instance=bookById)
    
    context = {
        'updateform': updatedBook
    }

    return render(request, 'pages/update.html', context)


# book delete function
def delete(request, id):
    
    deletedBook = get_object_or_404(Book, id=id)
    
    if request.method == 'POST':
        deletedBook.delete()
        return redirect('/')
    
    return render(request, 'pages/delete.html')