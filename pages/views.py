from django.shortcuts import render

from product.models import MainContent
from django.shortcuts import render

# 각 섹션에 보여줄 데이터 정의
SECTIONS = {
    'story': {
        'title': '브랜드 스토리',
        'heading': '창립 스토리',
        'text_blocks': [
            '우리 브랜드는 1990년 작은 가게에서 시작했습니다.',
            '초기 연혁을 살펴보면…'
        ],
        'tables': [
            {
                'caption': '연혁',
                'headers': ['연도', '이벤트'],
                'rows': [
                    ['1990', '첫 매장 오픈'],
                    ['2000', '전국 100호점 달성'],
                    ['2010', '해외 진출 시작'],
                ]
            }
        ],
        'images': [
            '/static/images/company/story_main.jpg',
            '/static/images/company/history_chart.png',
        ],
    },
    'process': {
        'title': '제조 과정',
        'heading': '생산 라인 소개',
        'text_blocks': [
            '최첨단 자동화 라인에서…',
            '각 공정 단계는 다음과 같습니다.'
        ],
        'images': [
            '/static/images/company/assembly_line.jpg',
            '/static/images/company/process_step1.png',
            '/static/images/company/process_step2.png',
        ],
    },
    'social': {
        'title': '사회 기여',
        'heading': '봉사 활동 사진',
        'text_blocks': [
            '매년 직원들과 함께…',
            '참여 방법은 아래와 같습니다.'
        ],
        'images': [
            '/static/images/company/volunteer1.jpg',
            '/static/images/company/volunteer2.jpg',
        ],
    }
}

def mainpage(request):
    # 최신순으로 정렬한 뒤 4개만 잘라서 전달
    featured = MainContent.objects.order_by('-pub_date')[:4]
    return render(request, 'pages/mainpage.html', {
        'featured': featured,
    })

def company(request, section='story'):
    data = SECTIONS.get(section, SECTIONS['story'])
    return render(request, 'pages/company.html', {
        'sections': SECTIONS,
        'current': section,
        'data': data,
    })

def product(request):
    return render(request, 'pages/product.html')

def guide(request):
    return render(request, 'pages/guide.html')

def news(request):
    # static/images/news 폴더 아래에 news1.jpg ~ news12.jpg를 놓으셨다고 가정
    image_files = [f'images/news/news{n}.jpg' for n in range(1, 13)]
    # 4개씩 묶어서 슬라이드 단위로
    slides = [image_files[i:i+4] for i in range(0, len(image_files), 4)]
    return render(request, 'pages/news.html', {
        'slides': slides,
    })

def event(request):
    return render(request, 'pages/event.html')

def support(request):
    return render(request, 'pages/support.html')
