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
from itertools import chain

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

def title_err(request):
    return render(request, 'blog/title_err.html', {})

def postJ_presentation(request):
    try:
        title = Title.objects.get(pk=currentPK)
    except ObjectDoesNotExist:
        return redirect('title_err')

    post_list = []
    for i in range(1,5):
        try:
            post = ((PostJ.objects.filter(ttl_index=str(currentPK)).filter(sub_index=str(i)).filter(published_date__isnull=False).latest('published_date')) )
            post_list.append(post)
        except ObjectDoesNotExist:
            post = None

    posts = iter(list(post_list))
    return render(request, 'blog/postj_presentation.html', {'posts': posts, 'title': title })

def postJ_detail(request, idx):
    index = int(idx)
    try:
        title = Title.objects.get(pk=currentPK)
    except ObjectDoesNotExist:
        return redirect('title_err')

    pbtn = 0
    post_list = []
    try:
        # posts = ((PostJ.objects.filter(ttl_index=str(currentPK)).filter(sub_index=idx).filter(or(author_org=User.objects.get(username='admin').latest('created_date'))
        #           Q(PostJ.objects.filter(ttl_index=str(currentPK)).filter(sub_index=idx).filter(author_org=User.objects.get(username='c')).latest('created_date')) )
        # posts = (Q(PostJ.objects.filter(ttl_index=str(currentPK)).filter(sub_index=idx).filter(author_org=User.objects.get(username='admin'))) |
        #          Q(PostJ.objects.filter(ttl_index=str(currentPK)).filter(sub_index=idx).filter(author_org=User.objects.get(username='c'))) )
        post = ((PostJ.objects.filter(ttl_index=str(currentPK)).filter(sub_index=idx).filter(author_org=User.objects.get(username='admin')).latest('created_date')) )
        post_list.append(post)
    except ObjectDoesNotExist:
        post = None

    try:
        post = ((PostJ.objects.filter(ttl_index=str(currentPK)).filter(sub_index=idx).filter(author_org=User.objects.get(username='c')).latest('created_date')) )
        post_list.append(post)
    except ObjectDoesNotExist:
        post = None

    try:
        postfind = PostJ.objects.filter(ttl_index=str(currentPK)).filter(sub_index=idx).filter(author_org=request.user).latest('created_date')
    except ObjectDoesNotExist:
        pbtn = 1

    posts = iter(list(post_list))
    return render(request, 'blog/postj_detail.html', {'posts': posts, 'title': title, 'idx': idx, 'pbtn':pbtn})

@login_required
def postJ_new(request, idx):
    index = int(idx)
    title = get_object_or_404(Title, pk=currentPK)
    if request.method == "POST":
        form = PostJForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_org = request.user
            post.author_rvs = request.user
            post.title_obj = title
            post.ttl_index = str(currentPK)
            post.sub_index = idx
            post.save()
            # index = (int(post.pk) -1) % topic_num +1
            # return redirect('postJ_detail', idx=str(index))
            return redirect('postJ_detail', idx=idx)
    else:
        form = PostJForm()
    return render(request, 'blog/postj_edit.html', {'form': form})

@login_required
def postJ_edit(request, pk):
    post = get_object_or_404(PostJ, pk=pk)
    if request.method == "POST":
        form1 = PostJForm(request.POST, instance=post)
        form2 = PostJForm()
        if form1.is_valid():
            post1 = form1.save(commit=False)
            post2 = form2.save(commit=False)
            post2.author_org = post1.author_org
            post2.author_rvs = request.user
            post2.title_obj = post1.title_obj
            post2.ttl_index = post1.ttl_index
            post2.sub_index = post1.sub_index
            post2.f_choice = post1.f_choice
            post2.text = post1.text
            post2.save()
            for comment in CommentJ.objects.filter(post=post1):
                comment.post = post2
                comment.save()
            # index = (int(post.pk) -1) % topic_num +1
            idx = post.sub_index
            return redirect('postJ_detail', idx=idx)
    else:
        form = PostJForm(instance=post)
    return render(request, 'blog/postj_edit.html', {'form': form})

@login_required
def postJ_publish(request, pk):
    post = get_object_or_404(PostJ, pk=pk)
    idx = post.sub_index
    post.publish()
    # index = (int(pk) -1) % topic_num +1
    return redirect('postJ_detail', idx=idx)

@login_required
def postJ_remove(request, pk):
    post = get_object_or_404(PostJ, pk=pk)
    idx = post.sub_index
    post.delete()
    # index = (int(pk) -1) % topic_num +1
    return redirect('postJ_detail', idx=idx)

def add_comment_to_postJ(request, pk):
    post = get_object_or_404(PostJ, pk=pk)
    if request.method == "POST":
        form = CommentJForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            # index = (int(post.pk) -1) % topic_num +1
            idx = post.sub_index
            return redirect('postJ_detail', idx=idx)
    else:
        form = CommentJForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def commentJ_approve(request, pk):
    comment = get_object_or_404(CommentJ, pk=pk)
    comment.approve()
    idx = comment.post.sub_index
    # index = (int(comment.post.pk) -1) % topic_num +1
    return redirect('postJ_detail', idx=idx)

@login_required
def commentJ_remove(request, pk):
    comment = get_object_or_404(CommentJ, pk=pk)
    # index = (int(comment.post.pk) -1) % topic_num +1
    idx = comment.post.sub_index
    comment.delete()
    return redirect('postJ_detail', idx=idx)
