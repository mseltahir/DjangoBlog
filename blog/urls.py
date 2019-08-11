from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path('', views.blog_page, name="blog_page"),
    path('<int:pk>', views.blog_detail, name='blog_detail'),
    path('<category>', views.blog_category, name='blog_category'),
    path('new', views.blog_new_post, name='blog_new_post')
]
