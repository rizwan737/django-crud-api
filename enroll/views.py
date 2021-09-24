from django.shortcuts import render,HttpResponseRedirect
from .forms import St
from .models import User


# Create your views here.

# this will add and show data
def add_show(request):
    stud = User.objects.all()
    if request.method == 'POST':
        fm = St(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = St()
            # fm.save()
    else:
        fm = St()
    return render(request, 'enroll/add.html', {'form': fm, 'stu': stud})
# This is will update data
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = St(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = St(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})



# This is will delete data
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')