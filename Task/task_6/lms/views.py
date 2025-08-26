from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Book, Issue
from django.utils import timezone

# 🏠 Dashboard / Home
def library_home(request):
    return render(request, "library.html")


# ➕ Add Student
def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("roll_number")
        course = request.POST.get("branch")
        year = request.POST.get("year")

        Student.objects.create(
            name=name,
            roll_number=roll,
            course=course,
            year=year
        )
        return HttpResponse("✅ Student Added Successfully")
    context = {"msg": "student added"}
    return render(request, "library.html", context)


# 👀 View Students
def view_students(request):
    students = Student.objects.all()
    return render(request, "library.html", {"students": students})


# ➕ Add Book
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        isbn = request.POST.get("isbn")
        total = request.POST.get("total_copies")

        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            total_copies=total,
            available_copies=total
        )
    context = {"msg": "book added"}
    return render(request, "library.html", context)


# 👀 View Books
def view_books(request):
    books = Book.objects.all()
    return render(request, "library.html", {"books": books})


# 📚 Issue Book
def issue_book(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        book_id = request.POST.get("book_id")

        try:
            student = Student.objects.get(roll_number=student_id)
            book = Book.objects.get(isbn=book_id)

            if book.available_copies > 0:
                Issue.objects.create(student=student, book=book)
                book.available_copies -= 1
                book.save()
                context = {"msg": "book issued successfully"}
            else:
                context = {"msg": "no book available"}
            
            return render(request, "library.html", context)
        except Exception as e:
            return HttpResponse(f"Error: {e}")


# 🔁 Reissue Book
def reissue_book(request):
    if request.method == "POST":
        issue_id = request.POST.get("issue_id")

        try:
            issue = Issue.objects.get(id=issue_id, return_date__isnull=True)
            issue.reissue_count += 1
            issue.issue_date = timezone.now()
            issue.save()
            return HttpResponse("🔁 Book Reissued Successfully")
        except:
            return HttpResponse("❌ Invalid Issue ID or Book Already Returned")

    return render(request, "reissue_book.html")


# 🔙 Return Book
def return_book(request):
    if request.method == "POST":
        issue_id = request.POST.get("issue_id")

        try:
            issue = Issue.objects.get(id=issue_id, return_date__isnull=True)
            issue.return_date = timezone.now()
            issue.save()

            book = issue.book
            book.available_copies += 1
            book.save()

            return HttpResponse("📦 Book Returned Successfully")
        except:
            return HttpResponse("❌ Invalid Issue ID")

    return render(request, "return_book.html")


# 🔍 Search Book by ID
def search_book(request):
    context = {}
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        try:
            book = Book.objects.get(isbn=book_id)
            issues = Issue.objects.filter(book=book, return_date__isnull=True)
            context = {"book": book, "issues": issues}
        except Book.DoesNotExist:
            return HttpResponse("❌ Book Not Found")

    return render(request, "library.html", context)
