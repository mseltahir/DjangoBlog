from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path('', views.PostListView.as_view(), name="blog_page"),
    path('<int:pk>/', views.PostDetailView.as_view(), name='blog_detail'),
    path('new/', views.PostCreateView.as_view(), name='blog_new_post'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='delete_post'),
]
