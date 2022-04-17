from django.forms import formset_factory
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from books.forms import BookForm
from books.models import Book


class ListBookView(View):
    def get(self, request):
        return render(request, 'list_book.html', context={'books': Book.objects.all().order_by('-created_at')})


class CreateBookView(View):
    def get(self, request):
        return render(request, 'create_book.html',
                      context={'forms': formset_factory(BookForm, extra=2)})

    def post(self, request):
        formset = formset_factory(BookForm)
        formset = formset(data=request.POST)

        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form.save()
            return redirect(to='list-books')

        else:
            return render(request, 'create_book.html',
                          context={'forms': formset})
