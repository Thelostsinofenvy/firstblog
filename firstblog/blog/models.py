from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    # only created users from the admin panel can create posts!
    author = models.ForeignKey('auth.user', on_delete=CASCADE)
    title = models.CharField(max_length=200)
    Text = models.TextField()
    date_created = models.DateTimeField(
        default=timezone.datetime.now, editable=True)

    # can be published later, so it doesn't need the parameter datetime.now()
    publish_date = models.DateTimeField(blank=True, null=True)

    # saving the date of publishing the Post.
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    # function to display title on the admin panel.
    def __str__(self):
        return self.title

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    # returns to post detail page.
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    posted_comments = models.ForeignKey(
        Post, related_name='comments', on_delete=CASCADE)  # comments for the posts.
    author = models.CharField(max_length=200, null=True)
    Text = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    # function to approve comments.
    def approve(self):
        if self.approved_comment == True:
            self.save()

    def get_absolute_url(self):
        return reverse("blog:post_list")
