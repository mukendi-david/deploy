from django.shortcuts import render
from .models import Student, Cotes
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required
def home(request):
    return render(request, 'verify/index.html')




@login_required
def view_cotes(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            student = Student.objects.get(code=code)
        except Student.DoesNotExist:
            msg = messages.error(request, 'Code invalide.')
            return redirect('verify:home')
        
        if student.user != request.user:
            msg = messages.error(request, "Vous n'êtes pas autorisé à accéder aux résultats de cet étudiant.")
            return redirect('verify:home')
        
        cotes = Cotes.objects.filter(student=student)
       
        context = {
            'student': student,
            'cotes': cotes,
            'demi' : 0
            
        }
    
    return render(request, 'verify/result.html', context)