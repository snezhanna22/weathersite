from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

from .models import News

@login_required
def show_all_news(request):
    search = request.GET.get('search', '')

    if search:
        post = News.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))
    else:
        post = News.objects.all()

    paginator = Paginator(post, 6)
    page_number = request.GET.get('page', 1)
    pages = paginator.get_page(page_number)

    is_paginated = pages.has_other_pages()

    if pages.has_previous():
        prev_url = f'?page={pages.previous_page_number()}'
    else:
        prev_url = ''

    if pages.has_next():
        next_url = f'?page={pages.next_page_number()}'
    else:
        next_url = ''

    context = {
        'title' : 'Новости',
        'post' : post,
        'page' : pages,
        'is_paginated' : is_paginated,
        'next_url' : next_url,
        'prev_url' : prev_url,
    }
    return render(request, 'news/news.html', context)


@login_required
def show_post(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    context = {
        'post' : post,
        'title' : post_slug
    }
    return render(request, 'news/page.html', context)