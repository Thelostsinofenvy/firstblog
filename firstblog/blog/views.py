from django.urls.base import reverse_lazy
from blog.forms import CommentForm
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.views.generic.edit import DeleteView
from blog.forms import PostForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from blog.models import Post, Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

# about page


class AboutView(TemplateView):
    template_name = 'base/about.html'

# list of posts


class PostListView(ListView):
    model = Post

    # queryset to get the posts published in decreasing order.
    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')


class PostDetailView(DetailView):
    model = Post

# creating a post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = 'login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

# updating a post


class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = 'login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

# deleting a post


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

# draft list for the non-published posts


class DraftListView(LoginRequiredMixin, ListView):
    login_url = 'login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    # queryset to get all the non -published posts

    def get_queryset():
        return Post.objects.filter(published_date__isnull=True).order_by('date_created')


##################################################
# For Comments
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", pk=post.pk)
        else:
            form = CommentForm()
            return render('blog/comment_form.html', {'form': form})

# approving comments


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish
    return redirect('post_detail', pk=pk)


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(request, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

# removing comments


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(request, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


def test(request):
    return render(request, "blog/base.html")
