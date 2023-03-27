from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter(trailing_slash=False)
router.register('get_recette', views.GetRecette, basename='get_recette')

urlpatterns = [
    path('/v1', include(router.urls)),
]