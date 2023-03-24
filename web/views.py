from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.urls import reverse

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not password:
        return render(request=request,
                    template_name='web/login.html',
                    context={'error_msg':'No available password',
                             'username': username or ''})
    if not username:
        return render(request=request,
            template_name='web/login.html',
            context={'error_msg':'No available username',
                     'password': password or ''})
    user = authenticate(request, username=username, password=password)
    if user is None:
        return render(request=request,
                      template_name='web/login.html',
                      context={'error_msg':'it Seems you connection as no available, if you think is an error, contact me at : x.trauchessec@groupe-aen.info'})
    login(user=user)
    return redirect(reverse('home'))

def home(request):
    return render(request, 'web/home.html')

def contact(request):
    return render(request, 'web/home.html')

def apis(request):
    return render(request=request, template_name='web/competence/api.html', context={})

def python(request):
    return render(request=request, template_name='web/competence/python.html', context={})