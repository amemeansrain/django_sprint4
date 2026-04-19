from django.shortcuts import render, get_object_or_404

from datetime import datetime

from .models import Post, Category


def index(request):
    template_name = 'blog/index.html'
    cur_time = datetime.now()
    post_list = Post.objects.select_related(
        'category'
    ).filter(
        pub_date__lte=cur_time,
        is_published=True,
        category__is_published=True
    ).order_by(
        '-pub_date'
    )[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    cur_time = datetime.now()
    post = get_object_or_404(
        Post.objects.select_related('category'),
        pk=id,
        pub_date__lte=cur_time,
        is_published=True,
        category__is_published=True
    )
    context = {
        'post': post,
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    cur_time = datetime.now()

    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    post_list = Post.objects.select_related(
        'category'
    ).filter(
        category=category,
        is_published=True,
        pub_date__lte=cur_time
    )
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template_name, context)
