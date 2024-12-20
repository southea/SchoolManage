from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from .DAO import models

def homePage(req):
    return render(req, 'home.html')
    
def instructorHome(req, id):
    context = dict()
    ins = models.Instructor.getById(id)

    context['ins'] = ins

    return render(req, 'insHome.html', context)
    
def instructorProfile(req, id):
    context = dict()
    ins = models.Instructor.getById(id)
    context['ins'] = ins
    return render(req, 'insProfile.html', context)
    
def instructorGrade(req, id):
    context = dict()
    ins = models.Instructor.getById(id)
    inss =models.Instructor.getAll()
    grades = models.Grade.getAll()
    context['ins'] = ins
    context['inss']=inss
    context['grades'] = grades
    return render(req, 'insGrade.html', context)

def instructorApplications(req, id):
    context = dict()
    ins = models.Instructor.getById(id)
    context['ins'] = ins
    context['applications'] = models.Application.getAllWithDetail()
    return render(req, 'insApplicationAll.html', context)

def instructorApplication(req, id):
    context = dict()
    ins = models.Instructor.getById(id)
    context['ins'] = ins
    context['applications'] = models.Application.getAllWithDetail()
    return render(req, 'insApplication.html', context)

def studentHome(req, id):
    context = dict()
    context['stu'] = models.Student.getById(id)
    context['inss']=models.Instructor.getAll()
    context['grades']=models.Grade.getAll()
    return render(req, 'stuHome.html', context)

def studentProfile(req, id):
    context = dict()
    context['stu'] = models.Student.getById(id)
    return render(req, 'stuProfile.html', context)

def studentApplication(req, id):
    context = dict()
    context['stu'] = models.Student.getById(id)
    context['inss'] = models.Instructor.getAll()
    context['applications'] = models.Application.getAllWithDetailByStuId(id)
    return render(req, 'stuApplication.html', context)

def studentApply(req, id):
    context = dict()
    context['stu'] = models.Student.getById(id)
    return render(req, 'stuApply.html', context)

def adminHome(req):
    context = dict()

    inss = models.Instructor.getAll()
    grades = models.Grade.getAll()

    context['inss'] = inss
    context['grades'] = grades
    return render(req, 'adminHome.html', context)

def adminAdd(req):
    context = dict()
    context['allIns'] = models.Instructor.getAll()
    context['allGrade'] = models.Grade.getAll()
    return render(req, 'adminAdd.html', context)

def adminDelete(req):
    context = dict()
    context['allStu'] = models.Student.getAll()
    context['allIns'] = models.Instructor.getAll()
    context['allGrade'] = models.Grade.getAll()
    return render(req, 'adminDelete.html', context)

def adminApplications(req):
    context = dict()
    context['applications'] = models.Application.getAllWithDetail()
    return render(req, 'adminApplicationAll.html', context)

def adminApplication(req):
    context = dict()
    context['applications'] = models.Application.getAllWithDetail()
    return render(req, 'adminApplication.html', context)

def adminEdit(req):
    context = dict()
    context['allStu'] = models.Student.getAll()
    context['allIns'] = models.Instructor.getAll()
    context['allGrade'] = models.Grade.getAll()
    return render(req, 'adminEdit.html', context)


