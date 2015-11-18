from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'noticias', views.NoticiaViewSet)
router.register(r'tipo-noticia', views.TipoNoticiaViewSet)
urlpatterns = [
    # Examples:
    # url(r'^$', 'django_backbone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(router.urls)),
    url(r'^$', views.home, name="home"),
]
