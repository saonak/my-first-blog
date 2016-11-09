from django.db import models
from django.utils import timezone

# Create your models here.
FMT_CHOICES = (
    ('TEXT', 'Text'),
    ('MARKDOWN', 'Markdown'),
)

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title   

class Post2(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    f_choice =  models.CharField(max_length=8, choices=FMT_CHOICES, default='TEXT',)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
        
class Comment(models.Model):
    post = models.ForeignKey('blog.Post2', related_name='comments')
#    author = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

######################### Jigsaw ####################################
class PostJ(models.Model):
    author_org = models.ForeignKey('auth.User', related_name='postj_au_org', default="")
    author_rvs = models.ForeignKey('auth.User', related_name='postj_au_rvs', default="")
    title_obj = models.ForeignKey('blog.Title', related_name='postj_ref', default=None)
    # ttl_index = models.IntegerField
    # sub_index = models.IntegerField
    ttl_index = models.CharField(max_length=4, default='1',)
    sub_index = models.CharField(max_length=4, default='1',)
    f_choice =  models.CharField(max_length=8, choices=FMT_CHOICES, default='TEXT',)
    text = models.TextField(default = "")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        if self.title_obj == None:
            return "..." + "_" + str(self.sub_index) + "_" + self.author_org + self.author_rvs + "_" + self.pk
        else:
            return self.title_obj.title + "_" + self.sub_index + "_" + "_" + str(self.pk)

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class CommentJ(models.Model):
    post = models.ForeignKey('blog.PostJ', related_name='comments')
#    author = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.post.title_obj.title + "_" + str(self.post.sub_index) + "_" + self.text[0:10] + "_"+ str(self.pk)

class Title(models.Model):
    author = models.ForeignKey('auth.User')
    title     = models.CharField(max_length=200)
    subtitle1 = models.CharField(max_length=200)
    subtitle2 = models.CharField(max_length=200)
    subtitle3 = models.CharField(max_length=200)
    subtitle4 = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + "_" + str(self.pk)
