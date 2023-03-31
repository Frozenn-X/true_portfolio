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
    context = {'menu_actif': 'home'}
    return render(request, 'web/home.html', context=context)


def about(request):
    context = {'menu_actif': 'about'}
    return render(request, 'web/about.html', context=context)


def contact(request):
    context = {'menu_actif': 'contact'}
    return render(request, 'web/contact.html', context=context)

def sql(request):
    return render(request=request, template_name='web/competence/sql.html', context={})

def apis(request):
    return render(request=request, template_name='web/competence/api.html', context={})

def python(request):
    return render(request=request, template_name='web/competence/python.html', context={})