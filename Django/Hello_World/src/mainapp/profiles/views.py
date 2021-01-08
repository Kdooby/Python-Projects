from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse
from .forms import ProfileForm
from .models import Profiles

# Create your views here.
def profile_console(request):
    profiles = Profiles.object.all()
    return render(request, 'profiles/profiles_page.html', {'profiles':profiles})

def details(request, pk):
    pk = int(pk)
    person = get_object_or_404(Profiles, pk=pk)
    form = ProfileForm(data=request.POST or None, instance = person)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('profile_console')
        else:
            print(form.errors)
    else:
        return render(request, 'profiles/present_profile.html', {'form':form})
    
def delete(request, pk):
    pk = int(pk)
    person = get_object_or_404(Profiles, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('profile_console')
    context = {'person':person,}
    return render(request, "profiles/confirmDelete.html", context)

def confirmed(request):
    if request.method == 'POST':
        # Creates form instance and binds to data
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('profile_console')
        else:
            return redirect('profile_console')

def createRecord(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile_console')
    else:
        print(form.errors)
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'profiles/createRecord.html', context)