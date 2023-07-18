from django.shortcuts import render, redirect
from djangomodelform.form import EmpForm


def home(request):
    if request.method == "post":
        student = EmpForm(request.post)
        if student.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:


       student = EmpForm()
       return render(request, 'index.html', {'form': student})
