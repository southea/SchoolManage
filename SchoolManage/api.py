import json
from datetime import datetime
from django.http.request import HttpRequest
from django.http.response import HttpResponse


from .DAO import models

def login(req : HttpRequest):
    username = req.POST.get('username')
    password = req.POST.get('password')
    thetype = int(req.POST.get('type'))
    result = False
    if thetype == 0:
        ins = models.Instructor.getById(username)
        if ins != None and ins.password == password:
            result = True
    elif thetype == 1:
        stu = models.Student.getById(username)
        if stu != None and stu.password == password:
            result = True
    elif thetype == 2:
        if username == 'admin' and password == 'admin':
            result = True
    return HttpResponse(json.dumps({'succeed': result}))

def insUpdate(req : HttpRequest):
    result = models.Instructor.updateInfo(req.POST.get('id'), req.POST.get('password'),req.POST.get('tele'))
    return HttpResponse(json.dumps({'succeed': result}))

def insConfirm(req : HttpRequest):
    result = models.Application.confirm(int(req.POST.get('id')), int(req.POST.get('is_agreed')))
    return HttpResponse(json.dumps({'succeed': result}))

def stuUpdate(req : HttpRequest):
    result = models.Student.updateInfo(req.POST.get('id'), req.POST.get('password'))
    return HttpResponse(json.dumps({'succeed': result}))

def stuApply(req : HttpRequest):
    result = True
    stu = models.Student.getById(int(req.POST.get('stu_id')))
    is_out = int(req.POST.get('is_out'))
    reason_site = req.POST.get('reason_site')
    result = models.Application.insert(stu.grade_id, stu.id, stu.ins_id, datetime.now(), reason_site, is_out)
    return HttpResponse(json.dumps({'succeed': result}))

def adminAddStu(req : HttpRequest):
    result = False
    msg = ''
    stu = models.Student.getById(req.POST.get('id'))
    ins = models.Instructor.getById(req.POST.get('ins_id'))
    if ins.grade_id != req.POST.get('grade_id'):
        msg = '辅导员与年级不对应，请重新选择'
    elif stu != None:
        msg = '该学号已存在'
    else:
        res = models.Student.insert(int(req.POST.get('id')), req.POST.get('name'), req.POST.get('password'), 
                                    req.POST.get('gender'), int(req.POST.get('age')), int(req.POST.get('grade_id')),
                                    int(req.POST.get('ins_id')))

        if res['succeed']:
            result = True
    return HttpResponse(json.dumps({'succeed': result, 'msg': msg}))

def adminAddIns(req : HttpRequest):
    result = False
    msg = ''
    ins = models.Instructor.getById(req.POST.get('id'))
    if ins != None:
        msg = '该职工号已存在'
    else:
        res = models.Instructor.insert(int(req.POST.get('id')), req.POST.get('name'), req.POST.get('password'),
                                       req.POST.get('gender'), req.POST.get('tele'), req.POST.get('grade_id'))
        if res['succeed']:
            result = True
    return HttpResponse(json.dumps({'succeed': result, 'msg': msg}))

def adminAddGrade(req : HttpRequest):
    result = False
    msg = ''
    grade = models.Grade.getById(req.POST.get('id'))
    if grade != None:
        msg = '该年级ID已存在'
    else:
        res = models.Grade.insert(int(req.POST.get('id')), req.POST.get('name'))
        if res['succeed']:
            result = True
    return HttpResponse(json.dumps({'succeed': result, 'msg': msg}))

def adminDeleteStu(req : HttpRequest):
    result = False
    msg = ''
    result = models.Student.delete(int(req.POST.get('id')))
    return HttpResponse(json.dumps({'succeed': result, 'msg': msg}))

def adminDeleteIns(req : HttpRequest):
    result = False
    msg = ''
    result = models.Instructor.delete(int(req.POST.get('id')))
    return HttpResponse(json.dumps({'succeed': result, 'msg': msg}))

def adminDeleteGrade(req : HttpRequest):
    result = False
    msg = ''
    result = models.Grade.delete(int(req.POST.get('id')))
    return HttpResponse(json.dumps({'succeed': result, 'msg': msg}))


def adminEditStu(req: HttpRequest):
    result = True
    msg = ''
    stu = models.Student.getById(req.POST.get('id'))
    ins = models.Instructor.getById(req.POST.get('ins_id'))
    if ins.grade_id != req.POST.get('grade_id'):
        msg = '辅导员与年级不对应，请重新选择'
    elif stu is None:
        msg = '该学号不存在'
        result = False
    else:
        res = models.Student.updateS(int(req.POST.get('id')), req.POST.get('name'), req.POST.get('password'),
                                    req.POST.get('gender'), int(req.POST.get('age')), int(req.POST.get('grade_id')),
                                    int(req.POST.get('ins_id')))
    return HttpResponse(json.dumps({'succeed': result, 'msg': msg}))

def adminEditIns(req : HttpRequest):
    result = True
    msg = ''
    ins = models.Instructor.getById(req.POST.get('id'))
    if ins is None:
        msg = '该职工号不存在'
        result = False
    else:
        res = models.Instructor.updateI(int(req.POST.get('id')), req.POST.get('name'), req.POST.get('password'),
                                       req.POST.get('gender'), req.POST.get('tele'), req.POST.get('grade_id'))

    return HttpResponse(json.dumps({'succeed': result, 'msg': msg}))

def adminEditGrade(req : HttpRequest):
    result = True
    msg = ''
    grade = models.Grade.getById(req.POST.get('id'))
    if grade is None:
        msg = '该年级ID不存在'
        result = False
    else:
        res = models.Grade.updateG(int(req.POST.get('id')), req.POST.get('name'))

    return HttpResponse(json.dumps({'succeed': result, 'msg': msg}))

