from django.db import models
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True, primary_key=True)
    course = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.roll_number})"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"


class Issue(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)
    reissue_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student.name} → {self.book.title}"
