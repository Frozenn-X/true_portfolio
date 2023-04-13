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
##############################################################################################################################
######################################################## PAGE GENERAL ########################################################
##############################################################################################################################
def home(request):
    context = {'menu_actif': 'home'}
    return render(request, 'web/home.html', context=context)

def about(request):
    context = {'menu_actif': 'about'}
    return render(request, 'web/about.html', context=context)

def contact(request):
    context = {'menu_actif': 'contact'}
    return render(request, 'web/contact.html', context=context)
##############################################################################################################################
#################################################### COMPETENCE TECHNIQUE ####################################################
##############################################################################################################################
def sql(request):
    return render(request=request, template_name='web/competence/technique/sql.html', context={})

def apis(request):
    return render(request=request, template_name='web/competence/technique/api.html', context={})

def python(request):
    return render(request=request, template_name='web/competence/technique/python.html', context={})

def bdd_relationnel(request):
    return render(request=request, template_name='web/competence/technique/bdd_relationnel.html', context={})

def research_and_dev(request):
    return render(request=request, template_name='web/competence/technique/R&D.html', context={})
##############################################################################################################################
##################################################### COMPETENCE HUMAINE #####################################################
##############################################################################################################################
def english(request):
    return render(request=request, template_name='web/competence/humaine/english.html', context={})

def communication(request):
    return render(request=request, template_name='web/competence/humaine/communication.html', context={})

def team_gestion(request):
    return render(request=request, template_name='web/competence/humaine/team_gestion.html', context={})

def project_gestion(request):
    return render(request=request, template_name='web/competence/humaine/project_gestion.html', context={})
##############################################################################################################################
######################################################## PAGE PROJECT ########################################################
##############################################################################################################################
def qualif_hierarchy(request):
    return render(request=request, template_name='web/my_projects/qualif_hierarchy.html', context={})

def wurth(request):
    return render(request=request, template_name='web/my_projects/wurth.html', context={})

def scraping_web(request):
    return render(request=request, template_name='web/my_projects/scraping_web.html', context={})

def sam_and_DLF(request):
    return render(request=request, template_name='web/my_projects/sam_and_DLF.html', context={})

def datactive(request):
    return render(request=request, template_name='web/my_projects/datactive.html', context={})

def generation_email(request):
    return render(request=request, template_name='web/my_projects/generation_email.html', context={})