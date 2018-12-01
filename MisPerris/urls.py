from django.conf.urls import url, include
from rest_framework import routers
from Api import views
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'Perrito', views.PerritosViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path( 'admin/', admin.site.urls ),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
