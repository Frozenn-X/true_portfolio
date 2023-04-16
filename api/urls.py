from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'get_recette', views.GetRecette, basename='get_recette')

# urlpatterns = router.urls
urlpatterns = []