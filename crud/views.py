from django.shortcuts import render, redirect
from .models import *
import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from crud.forms import *
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from .utils import render_to_pdf
from django.template.loader import get_template
import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from tablib import Dataset
from crud.resources import *


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def table(request):
    tabla1 = Persona.objects.all()
    tabla2 = AreaDeDesarrollo.objects.all()
    tabla3 = HistorialAcademico.objects.all()
    context = {'tabla1' : tabla1, 'tabla2': tabla2, 'tabla3': tabla3}
    
    return render(request, 'list.html', context )


@login_required
def create(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        member = Persona(
    nombre = request.POST['nombre'],
    apellido = request.POST['apellido'],
    rut = request.POST['rut'],
    dverificador = request.POST['dverificador'],
    telefono = request.POST['telefono'],
    fecha_nacimiento = request.POST['fecha_nacimiento'],
    correo = request.POST['correo'],
    direccion = request.POST['direccion'],
    ciudad = request.POST['ciudad'],
    nombre_foto=request.POST['nombre_foto'],
    foto=myfile.name,)
        member2 = HistorialAcademico(           
    estado = request.POST['estado'],
    carrera = request.POST['carrera'],
    año_ingreso = request.POST['año_ingreso'],
    año_salida = request.POST['año_salida'],)
        member3 = AreaDeDesarrollo(            
    cargo = request.POST['cargo'],
    nombre_empresa = request.POST['nombre_empresa'],
    experiencia_laboral = request.POST['experiencia_laboral'],
    ciudad = request.POST['ciudad'],)
        try:
            member.full_clean()
            member2.full_clean()
            member3.full_clean()
        except ValidationError as e:
            pass
        member.save()
        fkid = Persona.objects.latest('id_persona')
        member2.id_persona = fkid
        print(fkid)
        fkid2 = Persona.objects.latest('id_persona')
        member3.id_persona = fkid2
        print(fkid2)        
        member2.save()
        member3.save()       
        messages.success(request, 'Member was created successfully!')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return redirect('/list')
    else:      
        return render(request, 'add.html')
@login_required
def perfil(request, id_persona):
    perfils = Persona.objects.get(id_persona=id_persona)
    perfils2 = HistorialAcademico.objects.get(id_historial=id_persona)
    perfils3 = AreaDeDesarrollo.objects.get(id_a_desarrollo=id_persona)
    context = {'perfils': perfils, 'perfils2': perfils2, 'perfils3': perfils3}
    return render(request, 'perfil.html', context)
@login_required
def histrabajo(request, id_persona):
   
    perfils1 = Persona.objects.get(id_persona=id_persona)
    perfils3 = AreaDeDesarrollo.objects.filter(id_persona=id_persona)
    perfils2 = AreaDeDesarrollo.objects.get(id_a_desarrollo=id_persona)
    
    return render(request, 'histtrabajo.html', {'perfils1':perfils1,'perfils2':perfils2,'perfils3' : perfils3})

@login_required
def edit(request, id_persona):
    members = Persona.objects.get(id_persona=id_persona)
    members2 = HistorialAcademico.objects.get(id_historial=id_persona)
    members3 = AreaDeDesarrollo.objects.get(id_a_desarrollo=id_persona)
    context = {'members': members, 'members2': members2, 'members3': members3}
    return render(request, 'edit.html', context)


@login_required
def update(request, id_persona):
    member = Persona.objects.get(id_persona=id_persona)
    member2 = HistorialAcademico.objects.get(id_historial=id_persona)
    member3 = AreaDeDesarrollo.objects.get(id_a_desarrollo=id_persona)
    member2.estado = request.POST['estado']
    member2.carrera = request.POST['carrera']
    member2.año_ingreso = request.POST['año_ingreso']
    member2.año_salida = request.POST['año_salida']
    member.nombre = request.POST['nombre']
    member.apellido = request.POST['apellido']
    member.rut = request.POST['rut']
    member.dverificador = request.POST['dv']
    member.telefono = request.POST['telefono']
    member.fecha_nacimiento = request.POST['fecha_nacimiento']
    member.correo = request.POST['correo']
    member.direccion = request.POST['direccion']
    member3.nombre_empresa = request.POST['nombre_empresa']
    member3.cargo = request.POST['cargo']
    member3.experiencia_laboral = request.POST['experiencia_laboral']
    member3.ciudad = request.POST['ciudadempresa']
    member.ciudad = request.POST['ciudad']
    
    if "foto" in request.FILES:

        foto = request.FILES['foto']  
        member.foto.save(foto.name , foto)

    member.save()

    member2.save()
    member3.save()    
    messages.success(request, 'Persona fue actualizada exitosamente')
    return redirect('/list')
@login_required
def creartrabajo(request):
    if request.method == 'POST':

        member3 = AreaDeDesarrollo(
                
        cargo = request.POST['cargo'],
        nombre_empresa = request.POST['nombre_empresa'],
        experiencia_laboral = request.POST['experiencia_laboral'],
        ciudad = request.POST['ciudad'],
        id_persona_id = request.POST['id_persona'],
        
                )
        try:
            member3.full_clean()
        except ValidationError as e:
            pass
        member3.save()
        messages.success(request, 'Member was created successfully!')
        return redirect('/list')
    else:
        return render(request, 'editartrabajo.html')

@login_required
def trabajo(request, id_persona):
    
    
    members3 = AreaDeDesarrollo.objects.get(id_persona=id_persona)
  
    context = { 'members3': members3}
    return render(request, 'editartrabajo.html', context)

@login_required
def agregartrabajo(request, id_persona):
    
    member3 = AreaDeDesarrollo.objects.filter(id_persona=id_persona)
    
    member3.nombre_empresa = request.POST['nombre_empresa']
    member3.cargo = request.POST['cargo']
    member3.experiencia_laboral = request.POST['experiencia_laboral']
    member3.ciudad = request.POST['ciudad']

    #fkid = AreaDeDesarrollo.objects.latest('id_a_desarrollo')
    #member2.id_persona = fkid
    #print(fkid)
    member3.save()  
       
    messages.success(request, 'Persona fue actualizada exitosamente')
    return redirect('/list')

@login_required
def delete(request, id_persona):
    member = Persona.objects.get(id_persona=id_persona)
    member.delete()
    messages.error(request, 'Member was deleted successfully!')
    return redirect('/list')


@login_required
def generate_pdf(request):
    template = get_template('generarpdf.html')
    #response['Content-Disposition'] = f'inline; filename="file.pdf"'

    row = Persona.objects.all()
    
    context = {'row':row}
    html = template.render(context)
    #response.write(pdf)
    pdf = render_to_pdf('generarpdf.html',context)
    return HttpResponse(pdf,content_type="application/pdf")
@login_required
def generate_pdf_perfil(request, id_persona):
    template = get_template('generarpdfperfil.html')
    #response['Content-Disposition'] = f'inline; filename="file.pdf"'
    perfils = Persona.objects.get(id_persona=id_persona)
    perfils2 = HistorialAcademico.objects.get(id_historial=id_persona)
    perfils3 = AreaDeDesarrollo.objects.get(id_a_desarrollo=id_persona)
    context = {'perfils': perfils, 'perfils2': perfils2, 'perfils3': perfils3}
    #return render(request, 'perfil.html', context)
    #row = Persona.objects.all()
    
   # context = {'row':row}
    html = template.render(context)
    #response.write(pdf)
    pdf = render_to_pdf('generarpdfperfil.html',context)
    return HttpResponse(pdf,content_type="application/pdf")
   # return response

@login_required
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Listado_Estudiantes.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Rut', 'dv', 'Nombre', 'Apellido', 'Estado', 'Promoción' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Persona.objects.all().values_list('rut', 'dverificador', 'nombre', 'apellido', 'students__estado', 'students__año_ingreso')
  
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
  
    wb.save(response)
    return response

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                is_staff=True,
                is_active=True,
                is_superuser=True,
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def register_success(request):
    return render(request, 'success.html')

@login_required
def users(request):
    users_list = User.objects.all()
    paginator = Paginator(users_list, 5)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'users.html', {'users': users})


@login_required
def user_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    messages.error(request, 'User was deleted successfully!')
    return redirect('/users')

@login_required
def store(request):
    if 'GET' == request.method:
        exceldata = Persona.objects.all()
        context = {'exceldata': exceldata}
        return render(request, 'importar.html', context)
    try:
        
        person_resource = PersonaResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']
        imported_data = dataset.load(new_persons.read(), format='xlsx')
        print(imported_data)
        for data in imported_data:
            value = Persona(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],      
                )
            if data[0] == '':
                value.save()
            else:
                value.id_persona=data[0]
                value.save()

            value2 = AreaDeDesarrollo(
                data[12],
                data[13],
                data[14],
                data[15],
                data[16],
                data[17],
                data[18],
                data[19],               
                )
            value3 = HistorialAcademico(
                data[20],
                data[21],
                data[22],
                data[23],
                data[24],
                data[25], 
                )
         
            fkid = Persona.objects.latest('id_persona')
            value2.id_persona = fkid
            #print(fkid)
            value2.save()           
            
            fkid2 = Persona.objects.latest('id_persona')
            value3.id_persona = fkid2
            print(fkid2)
            value3.save() 
        result = person_resource.import_data(dataset, dry_run=True) # Test the data import  
        print(result.has_errors())           
        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now
        messages.success(request, "Archivo subido exitosamente")
        return redirect('/import')

    except Exception as e:
        messages.error(request, "Error al subir archivo" + e)
        return redirect('/import')

@login_required
def changePassword(request):
    print('changepasword')
    return render(request, 'change_password.html')


@login_required
def deleteFiles(request, id_persona):
    file = Persona.objects.get(id_persona=id_persona)
    file.delete()
    messages.error(request, 'User was deleted successfully!')
    return redirect('/fileupload')

