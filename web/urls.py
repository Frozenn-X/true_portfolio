from django.urls import path, include
from . import views

app_name = 'web'

urlpatterns = [
    # page where all start
    path('', views.home, name='home'),
    path('api/', include('api.urls')),
    path('index', views.home, name='home'),
    path('index/', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('home', views.home, name='home'),
    # page parcours
    path('parcours/', views.parcours, name='parcours'),
    path('parcours', views.parcours, name='parcours'),
    # page about
    path('about/', views.about, name='about'),
    path('about', views.about, name='about'),
    # page contact
    path('contact/', views.contact, name='contact'),
    path('contact', views.contact, name='contact'),
    # COMPETENCES
        ### TECHNIQUES
    path('api-desc', views.apis, name='api-desc'),
    path('python-desc', views.python, name='python-desc'),
    path('sql-desc', views.sql, name='sql-desc'),
    path('bdd_relationnal-desc', views.bdd_relationnel, name='bdd_relationnal-desc'),
    path('r&d-desc', views.research_and_dev, name='r&d-desc'),
        ### HUMAINES
    path('project-desc', views.project_gestion, name='project-desc'),
    path('team-desc', views.team_gestion, name='team-desc'),
    path('english-desc', views.english, name='english-desc'),
    path('comm-desc', views.communication, name='comm-desc'),
    # PROJECTS
    path('wurth-project', views.wurth, name='wurth-project'),
    path('SAM_DLF-project', views.sam_and_DLF, name='SAM_DLF-project'),
    path('datactive-project', views.datactive, name='datactive-project'),
    path('scraping-project', views.scraping_web, name='scraping-project'),
    path('generation_email-project', views.generation_email, name='generation_email-project'),
    path('hierarchy-project', views.qualif_hierarchy, name='hierarchy-project'),
]