from django.contrib.auth import REDIRECT_FIELD_NAME
from blog.forms import PostForm
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from blog.models import Post, Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class AboutView(TemplateView):
    template_name = 'base/about.html'


class PostListView(ListView):
    model = Post

    def get_queryset():
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = 'login/'
    REDIRECT_FIELD_NAME = 'blog/post_detail.html'
    form_class = PostForm
    model = Post
