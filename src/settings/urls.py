from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_backbone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^comentarios/', include('apps.comentarios.urls', namespace='comentarios')),
    url(r'', include('apps.publicaciones.urls', namespace='publicaciones')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
