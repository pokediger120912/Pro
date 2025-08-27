from django.shortcuts import render, redirect
from .models import Mod
from .forms import ModForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    mods = Mod.objects.all()
    return render(request, 'mods/index.html', {'mods': mods})

@login_required
def upload_mod(request):
    if request.method == 'POST':
        form = ModForm(request.POST, request.FILES)
        if form.is_valid():
            mod = form.save(commit=False)
            mod.author = request.user
            mod.save()
            return redirect('index')
    else:
        form = ModForm()
    return render(request, 'mods/upload_mod.html', {'form': form})
