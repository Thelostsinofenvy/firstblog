from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='post_detail'),
    path('post/new', views.CreatePostView.as_view(), name='post_new'),

]
