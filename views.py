from django.shortcuts import render
from modelformapp.forms import ProjectForm
from modelformapp.models import project

# Create your views here.
def index(request):
    return render(request,'modelForms/index.html')

def Listprojects(request):
    projectslist=project.objects.all()
    return render(request,'modelForms/listprojects.html',{'projects':projectslist})
def addproject(request):
    form= ProjectForm()
    if request.method == "POST":
        form =ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'modelForms/addproject.html',{'form':form})
