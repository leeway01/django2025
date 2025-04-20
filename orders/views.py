# orders/views.py
from django.shortcuts import render

def tracking(request):
    # 실제 로직 전에, 적어도 템플릿이 렌더링된다면 OK
    return render(request, 'orders/tracking.html')
