from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'get_recette', views.get_recette, basename='get_recette')

urlpatterns = router.urls