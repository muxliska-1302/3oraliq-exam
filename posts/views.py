from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from catalogs.models import Category
from authors.models import Author
from tags.models import Tag
from .models import Comment


def home(request):
    posts = Post.objects.all()
    catalogs = Category.objects.all()
    authors = Author.objects.all()
    tags = Tag.objects.all()
    category_id = request.GET.get('category')
    author_id = request.GET.get('author')
    tag_id = request.GET.get('tag')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    sort_by = request.GET.get('sort', 'latest')
    search = request.GET.get('query')
    if category_id:
        posts = posts.filter(category__id=category_id)
    if author_id:
        posts = posts.filter(author__id=author_id)
    if tag_id:
        posts = posts.filter(tags__id=tag_id)
    if start_date and end_date:
        posts = posts.filter(posted_at__range=(start_date, end_date))
    if start_date:
        posts = posts.filter(posted_at__gte=start_date)
    if end_date:
        posts = posts.filter(posted_at__lte=end_date)
    if sort_by == 'latest':
        posts = posts.order_by('-posted_at')
    elif sort_by == 'oldest':
        posts = posts.order_by('posted_at')
    if search:
        posts = posts.filter(title__icontains=search)
    ctx = {
        'posts':posts,
        'catalogs':catalogs,
        'authors':authors,
        'tags':tags,
        'sort_by':sort_by
    }
    return render(request, 'index_with_side_bar.html', ctx)

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        slug = slug,
        posted_at__year = year,
        posted_at__month = month,
        posted_at__day = day
    )
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        if name and email and comment:
            Comment.objects.create(
                post=post,
                name=name,
                email=email,
                comment=comment
            )
            return redirect('posts:detail', year=post.posted_at.year, month=post.posted_at.month, day=post.posted_at.day, slug=post.slug)
    comments = post.comments.all()
    ctx = {'post':post, 'comments':comments}
    return render(request, 'posts/post-detail.html', ctx)