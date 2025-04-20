from django.shortcuts import render
from .models import Students,Contact

# Create your views here.

def home(request):
    if request.method == "POST":
        print(request.POST.get('username'))
        
    students = Students.objects.all()
    context={
        "students":students
    }
    return render (request,'index.html',context)




def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if name and email and phone and message:
            Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            return render(request, 'contact.html', {'success': True})
        else:
            return render(request, 'contact.html', {'error': 'All fields are required.'})

    return render(request, 'contact.html')

