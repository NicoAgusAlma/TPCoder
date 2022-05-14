from django.http import HttpResponse
from django.shortcuts import render
from AppFamilia.models import Familiar
from django.template import Template, Context, loader

def familiar1(self):
    familiar1 = Familiar(nombre='Silvia',
    apellido='Almazan', 
    relacion='tia',
    edad=65,
    fechaNacimiento='1956-03-25'
    )
    familiar1.save()
    diccionario = {'nombre':familiar1.nombre, 'apellido':familiar1.apellido, 'relacion': familiar1.relacion, 'edad': familiar1.edad, 'fechaDeNacimiento': familiar1.fechaNacimiento}

    plantilla = loader.get_template('template.html')
    documento = plantilla.render(diccionario)
    

    return HttpResponse(documento)

def familiar2(self):
    familiar2 = Familiar(nombre='Eduardo',
    apellido='Almazan', 
    relacion='tio',
    edad=64,
    fechaNacimiento='1957-07-23'
    )
    familiar2.save()
    diccionario = {'nombre':familiar2.nombre, 'apellido':familiar2.apellido, 'relacion': familiar2.relacion, 'edad': familiar2.edad, 'fechaDeNacimiento': familiar2.fechaNacimiento}

    plantilla = loader.get_template('template2.html')
    documento = plantilla.render(diccionario)
    

    return HttpResponse(documento)

def familiar3(self):
    familiar3 = Familiar(nombre='Luis',
    apellido='Pratto', 
    relacion='primo',
    edad=35,
    fechaNacimiento='1986-09-11'
    )
    familiar3.save()
    diccionario = {'nombre':familiar3.nombre, 'apellido':familiar3.apellido, 'relacion': familiar3.relacion, 'edad': familiar3.edad, 'fechaDeNacimiento': familiar3.fechaNacimiento}

    plantilla = loader.get_template('template.html')
    documento = plantilla.render(diccionario)
    

    return HttpResponse(documento)
    
def familiar4(self):
    familiar4 = Familiar(nombre='Ana Maria',
    apellido='Lujan', 
    relacion='abuela',
    edad=86,
    fechaNacimiento='1932-12-19'
    )
    familiar4.save()
    diccionario = {'nombre':familiar4.nombre, 'apellido':familiar4.apellido, 'relacion': familiar4.relacion, 'edad': familiar4.edad, 'fechaDeNacimiento': familiar4.fechaNacimiento}

    plantilla = loader.get_template('template2.html')
    documento = plantilla.render(diccionario)
    

    return HttpResponse(documento)
    
def familiar5(self):
    familiar5 = Familiar(nombre='Felipe',
    apellido='Pipon', 
    relacion='hijo',
    edad=2,
    fechaNacimiento='2020-03-12'
    )
    familiar5.save()
    diccionario = {'nombre':familiar5.nombre, 'apellido':familiar5.apellido, 'relacion': familiar5.relacion, 'edad': familiar5.edad, 'fechaDeNacimiento': familiar5.fechaNacimiento}

    plantilla = loader.get_template('template.html')
    documento = plantilla.render(diccionario)
    

    return HttpResponse(documento)