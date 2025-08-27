from django.shortcuts import render, redirect
from .models import Mod
from .forms import ModForm
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    mods = Mod.objects.all()
    return render(request, 'mods/index.html', {'mods': mods})

def upload_mod(request):
    if request.method == 'POST':
        form = ModForm(request.POST, request.FILES)
        if form.is_valid():
            mod = form.save(commit=False)
            # This is a temporary solution. We will use the logged in user later.
            mod.author = User.objects.first()
            mod.save()
            return redirect('index')
    else:
        form = ModForm()
    return render(request, 'mods/upload_mod.html', {'form': form})
