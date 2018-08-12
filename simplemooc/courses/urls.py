from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<pk>\d+)/$', views.details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/inscricao/$', views.enrollment, name='enrollment'),
    url(r'^(?P<slug>[\w_-]+)/anuncios/$', views.announcements, name='announcements'),
    url(r'^(?P<slug>[\w_-]+)/cancelar-inscrição/$', views.undo_enrollment, name='undo_enrollment'),
    url(r'^(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)/$', views.show_announcement, name='show_announcement'),
    url(r'^(?P<slug>[\w_-]+)/aulas/$', views.lessons, name='lessons'),
    url(r'^(?P<slug>[\w_-]+)/aulas/(?P<pk>\d+)/$', views.lesson, name='lesson'),
    url(r'^(?P<slug>[\w_-]+)/material/(?P<pk>\d+)/$', views.material, name='material'),
]
