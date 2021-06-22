from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('blogs/',views.blog),
    path('blogpost/<int:id>',views.blogpost),
    path('add/',views.AddBlog.as_view()),
    path('search/',views.search),

]
