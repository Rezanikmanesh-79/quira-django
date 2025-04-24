from django.shortcuts import render

from library_management.models import Book


def booklist(request, author_age, book_age):
    books = Book.objects.all()
    good_books = []
    bad_books = []
    for book in books:
        if book.get_age().days // 365 < book_age:
            if book.author.get_age().days // 365 < author_age:
                good_books.append(book)
            else:
                bad_books.append(book)
        else:
            bad_books.append(book)
    return render(request, 'booklist.html', {
        'good_books': good_books,
        'bad_books': bad_books
    })
