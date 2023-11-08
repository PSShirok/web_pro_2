from django.urls import path

from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView
from products.views import ContactListView, HomeListView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blogpost_list'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail_post'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit_blog'),

]
