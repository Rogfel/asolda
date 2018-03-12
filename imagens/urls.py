from django.conf.urls import url
from django.conf import settings

from . import views

from .views import (
    ProjectList,
    ProjectDetail,
    ProjectCreation,
    ProjectUpdate,
    ProjectDelete,

    ImageList,
    ImageDetail,
    ImageCreation,
    ImageUpdate,
    ImageDelete
)
urlpatterns = [

    # project
    url(r'^$', ProjectList.as_view(), name='project-list'),
    url(r'^new$', ProjectCreation.as_view(), name='project-new'),
    url(r'^(?P<slug>[\w-]+)$', ProjectDetail.as_view(), name='project-detail'),
    url(r'^edit/(?P<slug>[\w-]+)$',
        ProjectUpdate.as_view(),
        name='project-edit'),
    url(r'^delete/(?P<slug>[\w-]+)$',
        ProjectDelete.as_view(),
        name='project-delete'),

    # image
    url(r'^(?P<slug_proy>[\w-]+)/images$',
        ImageList.as_view(), name='image-list'),
    url(r'^(?P<slug_proy>[\w-]+)/image/new$',
        ImageCreation.as_view(), name='image-new'),
    url(r'^(?P<slug_proy>[\w-]+)/image/(?P<slug>[\w-]+)$',
        ImageDetail.as_view(), name='image-detail'),
    url(r'^(?P<slug_proy>[\w-]+)/image/edit/(?P<slug>[\w-]+)$',
        ImageUpdate.as_view(), name='image-edit'),
    url(r'^(?P<slug_proy>[\w-]+)/image/delete/(?P<slug>[\w-]+)$',
        ImageDelete.as_view(), name='image-delete'),
    url(r'^(?P<slug_proy>[\w-]+)/image/analisys/(?P<slug>[\w-]+)$',
        ImageDetail.as_view(), name='image-analisys'),

    # media    
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

]
