from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobrenosotros/', views.about, name='about'),
    path('SolicitudEmpresa/', views.ListaSolicitudesVista.as_view(), name="SolicitudEmpresa"),
    path('SolicitudEmpresa/<pk>', views.ListaSolicitudesVista.as_view(), name="solicitudempresa-detail"),
]

urlpatterns+=[
   
    path('contacto/', views.SolicitudEmpresaCreate.as_view(), name="contact"),
    path('SolicitudEmpresa/<pk>/delete/', views.SolicitudEmpresaDelete.as_view(), name="SolicitudEmpresa_delete"),
    path('SolicitudEmpresa/<pk>/update/', views.SolicitudEmpresaUpdate.as_view(), name="SolicitudEmpresa_update"),

]