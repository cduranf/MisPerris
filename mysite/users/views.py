from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Tu cuenta ha sido creada, ahora pueden iniciar sesión')
            return redirect('post_list')
    else:
        form = UserRegisterForm()

    return render(request,'users/registrar.html', {'form': form})
