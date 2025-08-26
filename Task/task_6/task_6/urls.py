"""
URL configuration for task_6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lms import views

    
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.library_home, name="library_dashboard"),
    path("add-student/", views.add_student, name="add_student"),
    path("view-student/", views.view_students, name="view_student"),
    path("add-book/", views.add_book, name="add_book"),
    path("view-books/", views.view_books, name="view_books"),
    path("issue-book/", views.issue_book, name="issue_book"),
    path("return-book/", views.return_book, name="return_book"),
    path("reissue-book/", views.reissue_book, name="reissue_book"),
    path("search-book/", views.search_book, name="search_book"),
]
