from multiprocessing import context
from django.shortcuts import render
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.POST:
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = UserRegisterForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)
