# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    rut = models.IntegerField()
    dverificador = models.TextField()
    nombre = models.TextField()
    apellido = models.TextField()
    fecha_nacimiento = models.TextField()
    foto = models.ImageField()
    nombre_foto = models.CharField(max_length=255, blank=True)
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.TextField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    ciudad = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.id_persona)

    class Meta:
        managed = False
        db_table = 'Persona'


class AreaDeDesarrollo(models.Model):
    id_a_desarrollo = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey('Persona', on_delete=models.CASCADE, db_column='id_persona', editable=False, related_name='studentst')
    cargo = models.TextField(blank=True, null=True)
    nombre_empresa = models.TextField(blank=True, null=True)
    experiencia_laboral = models.TextField(blank=True, null=True)
    ciudad = models.TextField(blank=True, null=True)
    fecha_creacion = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.id_persona)

    class Meta:
        
        db_table = 'AreaDeDesarrollo'


class HistorialAcademico(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey('Persona', on_delete=models.CASCADE, db_column='id_persona',  editable=False, related_name='students')
    
    año_ingreso = models.IntegerField(blank=True, null=True)
    año_salida = models.IntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    carrera = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.id_persona)

    class Meta:
       
        db_table = 'HistorialAcademico'




class Lista(models.Model):
    rut = models.IntegerField(blank=True, null=True)
    dverificador = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    apellido = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.TextField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    ciudad = models.TextField(blank=True, null=True)
    correo = models.TextField(blank=True, null=True)
    telefono = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    año_ingreso = models.IntegerField(blank=True, null=True)
    año_salida = models.TextField(blank=True, null=True)
    carrera = models.TextField(blank=True, null=True)
    nombre_empresa = models.TextField(blank=True, null=True)
    cargo = models.TextField(blank=True, null=True)
    experiencia_laboral = models.TextField(blank=True, null=True)
    ciudad_empresa = models.TextField(blank=True, null=True)
    fecha_creacion = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.TextField(blank=True, null=True)
    linkedin = models.TextField(db_column='Linkedin', blank=True, null=True)  # Field name made lowercase.
    id_persona = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='media')
    nombre_foto = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return '{}'.format(self.id_persona)

    class Meta:
        managed = False
        db_table = 'Lista'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    mobile_number = models.CharField(max_length=10, blank=True)
    description = models.TextField(max_length=255, blank=False)
    location = models.TextField(max_length=255, blank=False)
    date = models.DateField('%m/%d/%Y')
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.CharField(max_length=255, )
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Ajax(models.Model):
    text = models.CharField(max_length=255, blank=True)
    search = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class CsvUpload(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    end_date = models.DateTimeField()
    notes = models.CharField(max_length=255, blank=True)
