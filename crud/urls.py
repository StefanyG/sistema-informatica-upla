from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^creartrabajo$', views.creartrabajo, name='creartrabajo'),
    url(r'^list$', views.table, name='list'),
    url(r'^import$', views.store, name='import'),
    url(r'^edit/(?P<id_persona>\d+)$', views.edit, name='edit'),
    url(r'^trabajo/(?P<id_persona>\d+)$', views.trabajo, name='trabajo'),
    url(r'^trabajo/agregartrabajo/(?P<id_persona>\d+)$', views.agregartrabajo, name='agregartrabajo'),
    url(r'^perfil/(?P<id_persona>\d+)$', views.perfil, name='perfil'),
    url(r'^perfil/historial/(?P<id_persona>\d+)$', views.histrabajo, name='historial'),
    url(r'^edit/update/(?P<id_persona>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id_persona>\d+)$', views.delete, name='delete'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$',views.register_success,name='register_success'),
    url(r'^users/$',views.users,name='users'),
    url(r'^users/delete/(?P<id>\d+)$', views.user_delete, name='user_delete'),
    url(r'^change_password$', views.changePassword, name='changePassword'),
    url(r'^file/delete$', views.changePassword, name='changePassword'),
    url(r'^file/delete/(?P<id_persona>\d+)$', views.deleteFiles, name='deleteFiles'),
    url(r'^generate-pdf$', views.generate_pdf, name='generate-pdf'),
    url(r'^generate-pdf-perfil/(?P<id_persona>\d+)$', views.generate_pdf_perfil, name='generate-pdf-perfil'),
    url(r'^export_users_xls$', views.export_users_xls, name='export_users_xls'),
]