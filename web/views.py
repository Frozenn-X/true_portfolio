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
    return render(request, 'web/home.html', context={'menu_actif': 'home'})


def about(request):
    return render(request, 'web/about.html', context={'menu_actif': 'about'})

def parcours(request):
    return render(request, 'web/parcours.html', context={'menu_actif': 'parcours'})

def parcoursbis(request):
    return render(request, 'web/parcours-bis.html', context={'menu_actif': 'parcours'})

def contact(request):
    return render(request, 'web/contact.html', context={'menu_actif': 'contact'})


##############################################################################################################################
#################################################### COMPETENCE TECHNIQUE ####################################################
##############################################################################################################################

def sql(request):
    return render(request=request, template_name='web/competence/technique/sql.html', context={'menu_actif': 'sql'})


def apis(request):
    return render(request=request, template_name='web/competence/technique/api.html', context={'menu_actif': 'apis'})


def python(request):
    return render(request=request, template_name='web/competence/technique/python.html', context={'menu_actif': 'python'})


def bdd_relationnel(request):
    return render(request=request, template_name='web/competence/technique/bdd_relationnel.html', context={'menu_actif': 'bdd'})


def research_and_dev(request):
    return render(request=request, template_name='web/competence/technique/R&D.html', context={'menu_actif': 'r&d'})


##############################################################################################################################
##################################################### COMPETENCE HUMAINE #####################################################
##############################################################################################################################

def english(request):
    return render(request=request, template_name='web/competence/humaine/english.html', context={'menu_actif': 'english'})


def communication(request):
    return render(request=request, template_name='web/competence/humaine/communication.html', context={'menu_actif': 'communication'})


def team_gestion(request):
    return render(request=request, template_name='web/competence/humaine/team_gestion.html', context={'menu_actif': 'team'})


def project_gestion(request):
    return render(request=request, template_name='web/competence/humaine/project_gestion.html', context={'menu_actif': 'project'})


##############################################################################################################################
######################################################## PAGE PROJECT ########################################################
##############################################################################################################################

def qualif_hierarchy(request):
    return render(request=request, template_name='web/my_projects/qualif_hierarchy.html', context={'menu_actif': 'hierarchy-project'})

def wurth(request):
    return render(request=request, template_name='web/my_projects/wurth.html', context={'menu_actif': 'wurth-project'})

def scraping_web(request):
    return render(request=request, template_name='web/my_projects/scraping_web.html', context={'menu_actif': 'scraping-project'})

def sam_and_DLF(request):
    return render(request=request, template_name='web/my_projects/sam_and_DLF.html', context={'menu_actif': 'SAM_DLF-project'})

def datactive(request):
    return render(request=request, template_name='web/my_projects/datactive.html', context={'menu_actif': 'datactive-project'})

def generation_email(request):
    return render(request=request, template_name='web/my_projects/generation_email.html', context={'menu_actif': 'generation_email-project'})