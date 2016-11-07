from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post
from .models import Post2, Comment
from .models import Title, PostJ, CommentJ
from .forms import PostForm
from .forms import PostForm2, CommentForm
from .forms import TitleForm, PostJForm, CommentJForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

# Global parameter
currentPK = 1  # PK number for current topic
topic_num = 4  # how many of the subtitle

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

#####

def post_list2(request):
    posts = Post2.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail2(request, pk):
    post = get_object_or_404(Post2, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new2(request):
    if request.method == "POST":
        form = PostForm2(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm2()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit2(request, pk):
    post = get_object_or_404(Post2, pk=pk)
    if request.method == "POST":
        form = PostForm2(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm2(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    
@login_required
def post_draft_list2(request):
    admin_user= User.objects.get(username='admin')
    if request.user != admin_user:
        posts = Post2.objects.filter(Q(author=request.user)).filter(published_date__isnull=True).order_by('created_date')
    else:
        posts = Post2.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish2(request, pk):
    post = get_object_or_404(Post2, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove2(request, pk):
    post = get_object_or_404(Post2, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post2, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)

def title_list(request):
    try:
        title = Title.objects.get(pk=currentPK)
    except ObjectDoesNotExist:
        title = None

    return render(request, 'blog/title_list.html', {'title': title})

@login_required
def title_edit(request):
    try:
        title = Title.objects.get(pk=currentPK)
    except ObjectDoesNotExist:
        title = None
    if request.method == "POST":
        if title == None:
            form = TitleForm(request.POST)
        else:
            form = TitleForm(request.POST, instance=title)
        if form.is_valid():
            titles = form.save(commit=False)
            titles.author = request.user
            titles.pk = currentPK
            titles.save()
            titles.publish()
            return redirect('title_list')
    else:
        if title == None:
            form = TitleForm()
        else:
            form = TitleForm(instance=title)
    return render(request, 'blog/title_edit.html', {'form': form})

def postJ_detail(request, idx):
    index = int(idx)
    try:
        post = PostJ.objects.get(pk=((currentPK-1)*topic_num+index))
    except ObjectDoesNotExist:
        if   index == 1:
            subttl = Title.objects.get(pk=currentPK).subtitle1
        elif index == 2:
            subttl = Title.objects.get(pk=currentPK).subtitle2
        elif index == 3:
            subttl = Title.objects.get(pk=currentPK).subtitle3
        else: # index==4:
            subttl = Title.objects.get(pk=currentPK).subtitle4
        post = PostJ.objects.create(author = request.user,
                                    title = Title.objects.get(pk=currentPK).title,
                                    subtitle = subttl,
                                    pk=((currentPK-1)*topic_num+index))
    return render(request, 'blog/postj_detail.html', {'post': post})

@login_required
def postJ_edit(request, pk):
    post = get_object_or_404(PostJ, pk=pk)
    if request.method == "POST":
        form = PostJForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            index = int(post.pk) % topic_num
            return redirect('postJ_detail', idx=str(index))
    else:
        form = PostJForm(instance=post)
    return render(request, 'blog/postj_edit.html', {'form': form})

@login_required
def postJ_publish(request, pk):
    post = get_object_or_404(PostJ, pk=pk)
    post.publish()
    index = int(pk)%topic_num
    return redirect('postJ_detail', idx=str(index))

@login_required
def postJ_remove(request, pk):
    post = get_object_or_404(PostJ, pk=pk)
    post.delete()
    index = int(pk)%topic_num
    return redirect('postJ_detail', idx=str(index))

def add_comment_to_postJ(request, pk):
    post = get_object_or_404(PostJ, pk=pk)
    if request.method == "POST":
        form = CommentJForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            index = int(post.pk) % topic_num
            return redirect('postJ_detail', idx=str(index))
    else:
        form = CommentJForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def commentJ_approve(request, pk):
    comment = get_object_or_404(CommentJ, pk=pk)
    comment.approve()
    index = int(comment.post.pk)%topic_num
    return redirect('postJ_detail', idx=str(index))

@login_required
def commentJ_remove(request, pk):
    comment = get_object_or_404(CommentJ, pk=pk)
    index = int(comment.post.pk)%topic_num
    comment.delete()
    return redirect('postJ_detail', idx=str(index))
