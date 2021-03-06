from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from bpinfo import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'bpinfo', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'blockproducer', views.BlockProducerViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls))
]
