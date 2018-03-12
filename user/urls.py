from django.conf.urls import url

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    # user
    url(r'^', auth_views.login, {'template_name': 'login2.html'}, name='login'),
    # url(r'^perfil/$', auth_views.perfil, {'template_name': 'perfil.html'}, name='perfil'),
    url(r'^logout/', views.my_logout, name='logout'),
    # url(r'^$', views.homelogin(), name='url_login'),
    # url(r'^login$', views.userlogin(), name='perfil')
]
