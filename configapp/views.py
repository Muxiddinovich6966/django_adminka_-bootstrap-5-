
from django.shortcuts import render
from .models import Student, Kurs

def app(request):
    talabalar = Student.objects.all()
    kurslar = Kurs.objects.all()

    context = {
        "talabalar": talabalar,
        "kurslar": kurslar,
        "title": "Talabalar va Kurslar"
    }

    return render(request, 'Student/app.html', context=context)
