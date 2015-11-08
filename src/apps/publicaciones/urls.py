from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'publicaciones', views.NoticiaViewSet)
urlpatterns = [
    # Examples:
    # url(r'^$', 'django_backbone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(router.urls)),
]
