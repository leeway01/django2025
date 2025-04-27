from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from .models import MainContent, Comment
from .forms import CommentForm

def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    return render(request, 'product/content_list.html', {'content_list': content_list})

def detail(request, content_id):
    content = get_object_or_404(MainContent, pk=content_id)
    return render(request, 'product/content_detail.html', {'content_list': content})

@login_required(login_url='accounts:login')
def comment_create(request, content_id):
    content = get_object_or_404(MainContent, pk=content_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = content
            comment.author = request.user
            comment.save()
            return redirect('product:detail', content_id=content.id)
    else:
        form = CommentForm()
    return render(request, 'product/content_detail.html', {
        'content_list': content,
        'form': form,
    })

@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('product:detail', content_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'product/comment_form.html', {
        'form': form,
        'comment': comment,
    })

@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    content_id = comment.content_list.id
    comment.delete()
    return redirect('product:detail', content_id=content_id)

def product_list(request, category=None):
    # 1) 카테고리 필터
    qs = MainContent.objects.all()
    if category:
        qs = qs.filter(category=category)

    # 2) 인기순 상위 2개, 그 외는 최신순
    popular = qs.order_by('-sales_count')[:2]
    latest  = qs.order_by('-pub_date')[2:]

    context = {
        'categories': [c for c,_ in MainContent._meta.get_field('category').choices],
        'current_category': category or '전체',
        'popular_products': popular,
        'latest_products': latest,
    }
    return render(request, 'product/product_list.html', context)

def product_order(request, product_id):
    product = get_object_or_404(MainContent, pk=product_id)
    # TODO: 실제 결제 로직 / 외부 연동 호출
    # 지금은 단순히 주문 확인 페이지만 띄우는 예시
    return render(request, 'product/product_order.html', {'product': product})