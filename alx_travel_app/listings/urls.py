from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'listings', views.ListingViewSet)

app_name = 'listings'

urlpatterns = [
    path('', include(router.urls)),
]