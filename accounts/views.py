from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


from .forms import UserCreationForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        # print(username, pass1)

        user = authenticate(request, username=username, password=pass1)
        if not user:
            context = {'error': 'Invalid username or password!'}
            return render(request, 'login.html', context)
        
        login(request, user)
        return redirect('/')

    return render(request, 'login.html', {})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return render(request, 'logout.html', {})


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_form = form.save()
        messages.success(request, 'Sign up successful. Please log in.')
        return redirect('login')

    return render(request, 'register.html', {'form': form})

