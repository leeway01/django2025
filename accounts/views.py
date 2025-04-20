from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')   # 또는 URL 네임스페이스를 쓰고 있다면: redirect('index')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {
        'form': form
    })
