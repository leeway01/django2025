from django.shortcuts import render

from product.models import MainContent
from django.shortcuts import render

def mainpage(request):
    # 최신순으로 정렬한 뒤 4개만 잘라서 전달
    featured = MainContent.objects.order_by('-pub_date')[:4]
    return render(request, 'pages/mainpage.html', {
        'featured': featured,
    })

def company(request):
    return render(request, 'pages/company_info.html')

def product(request):
    return render(request, 'pages/product.html')

def guide(request):
    return render(request, 'pages/guide.html')

def news(request):
    return render(request, 'pages/news.html')

def event(request):
    return render(request, 'pages/event.html')

def support(request):
    return render(request, 'pages/support.html')
