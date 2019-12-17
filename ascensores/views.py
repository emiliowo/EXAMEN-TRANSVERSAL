from django.shortcuts import render
from .models import SolicitudEmpresa
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

class ListaSolicitudesVista(generic.ListView):
    model	=	SolicitudEmpresa
    context_object_name ='solicitudempresa_list' 
    template_name =	'ascensores/solicitudempresa_list.html'


class SolicitudEmpresaCreate(CreateView):
    model = SolicitudEmpresa
    fields= '__all__'


class SolicitudEmpresaUpdate(UpdateView):
    model = SolicitudEmpresa
    fields = ['nombreEmp','email','direccion']


class SolicitudEmpresaDelete(DeleteView):
    model = SolicitudEmpresa
    success_url= reverse_lazy('SolicitudEmpresa')

class SolicitudEmpresaDetailView(generic.DeleteView):
    model = SolicitudEmpresa  