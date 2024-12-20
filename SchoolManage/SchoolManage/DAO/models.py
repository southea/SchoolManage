from . import database


class Grade:
    def __init__(self):
        self.id = -1
        self.name = ''
        self.is_delete = 0

    @staticmethod
    def getAll():
        queries = database.doQuery("select * from grade where grade_is_delete=0")
        res = []
        for q in queries['data']:
            res.append(Grade.convertToObj(q))   #append()向列表末尾添加元素
        return res

    @staticmethod
    def getById(id):
        grade = None
        query = database.doQuery("select * from grade where grade_id='{0}' and grade_is_delete=0".format(id))
        if len(query['data']) > 0:
            grade = Grade.convertToObj(query['data'][0])
        return grade


    @staticmethod
    def insert(id, name):
        result = dict()
        if(id.isdigit() and len(id)==4):
            result = database.doInsert("insert into grade values('{0}', '{1}', '{2}')".format(id, name, 0))
        else :
            result['succeed'] = False
        return result

    @staticmethod
    def delete(id):
        result = database.doUpdate("update grade set grade_is_delete=1 where grade_id='{0}'".format(id))
        return result['succeed']

    @staticmethod
    def updateG(id, name):
        result = dict()
        if(id.isdigit() and len(id)==4):
            result = database.doUpdate("update grade set grade_name='{0}' where grade_id='{1}'".format(name, id))
        else :
            result['succeed'] = False
        return result['succeed']


    @staticmethod
    def convertToObj(queryTuple):
        grade = Grade()
        grade.id = queryTuple[0]
        grade.name = queryTuple[1]
        grade.is_delete = queryTuple[2]
        return grade


class Instructor:
    def __init__(self):
        self.id = -1
        self.name = ''
        self.password = ''
        self.gender = ''
        self.is_delete = 0
        self.tele = ''
        self.grade_id = 0

    @staticmethod
    def getAll():
        queries = database.doQuery("select * from instructor where ins_is_delete=0")
        res = []
        for q in queries['data']:
            res.append(Instructor.convertToObj(q))
        return res

    @staticmethod
    def getById(id):
        ins = None
        query = database.doQuery("select * from instructor where ins_id='{0}' and ins_is_delete=0".format(id))
        if len(query['data']) > 0:
            ins = Instructor.convertToObj(query['data'][0])
        return ins

    @staticmethod
    def updateInfo(id, password, tele):
        result = dict()
        if(tele.isdigit() and len(tele)==11):
            result = database.doUpdate("update instructor set ins_password='{0}',ins_tele='{1}' where ins_id='{2}'".format(password, tele, id))
        else :
            result['succeed'] = False
        return result['succeed']

    @staticmethod
    def updateI(id, name, password, gender, tele, grade_id):
        result = dict()
        if(tele.isdigit() and len(tele)==11):
            result = database.doUpdate("update instructor set ins_name='{0}' ins_password='{1}', ins_gender='{2}', ins_tele='{3}', ins_grade_id='{4}' where ins_id={5}".format(name, password, gender, tele, grade_id, id))
        else :
            result['succeed'] = False
        return result['succeed']


    @staticmethod
    def insert(id, name, password, gender, tele, grade_id):
        result = dict()
        if(tele.isdigit() and len(tele)==11 and id.isdigit() and len(id)==6):
            result = database.doInsert("insert into instructor values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(id, name, password, gender, 0, tele, grade_id))
        else:
            result['succeed'] = False
        return result

    @staticmethod
    def delete(id):
        result = database.doUpdate("update instructor set ins_is_delete=1 where ins_id='{0}'".format(id))
        return result['succeed']

    @staticmethod
    def convertToObj(queryTuple):
        ins = Instructor()
        ins.id = queryTuple[0]
        ins.name = queryTuple[1]
        ins.password = queryTuple[2]
        ins.gender = queryTuple[3]
        ins.is_delete = queryTuple[4]
        ins.tele = queryTuple[5]
        ins.grade_id = queryTuple[6]
        return ins


class Student:
    def __init__(self):
        self.id = -1
        self.name = ''
        self.password = ''
        self.gender = ''
        self.is_delete = 0
        self.age = 0
        self.grade_id = 0
        self.ins_id = 0

    @staticmethod
    def getAll():
        queries = database.doQuery("select * from student where stu_is_delete=0")
        res = []
        for q in queries['data']:
            res.append(Student.convertToObj(q))
        return res

    @staticmethod
    def getById(id):
        stu = None
        query = database.doQuery("select * from student where stu_id='{0}' and stu_is_delete=0".format(id))
        if len(query['data']) > 0:
            stu = Student.convertToObj(query['data'][0])
        return stu

    @staticmethod
    def getIns(id):
        query = database.doQuery("select * from instructor where ins_id in (select * from student where stu_id='{0}' and stu_is_delete=0) and ins_is_delete=0 ".format(id))
        ins = None
        if len(query['data']) > 0:
            ins = Instructor.convertToObj(query['data'][0])
        return ins

    @staticmethod
    def updateInfo(id, password):
        result = database.doUpdate("update student set stu_password='{0}' where stu_id='{1}'".format(password, id))
        return result['succeed']

    @staticmethod
    def insert(id, name, password, gender, age, ins_id):
        result = dict()
        if(age.isdigit() and age>3 and age<100 and id.isdigit() and len(id)==12):
            result = database.doInsert("insert into student values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}',(select ins_grade_id from instructor where ins_id='{6}' and ins_is_delete=0), '{6}')".format(id, name, password, gender, 0, age, ins_id))
        else:
            result['succeed'] = False
        return result

    @staticmethod
    def updateS(id, name, password, gender, age, ins_id):
        result = dict()
        if(age.isdigit() and age>3 and age<100) :
            result = database.doUpdate("update student set stu_name='{0}', stu_password='{1}', stu_gender='{2}', stu_age='{3}', stu_grade_id=(select ins_grade_id from instructor where ins_id='{4}' and ins_is_delete=0), stu_ins_id='{4}' where stu_id='{5}'".format(name, password, gender, age, ins_id, id))
        else:
            result['succeed'] = False
        return result['succeed']


    @staticmethod
    def delete(id):
        result = database.doUpdate("update student set stu_is_delete=1 where stu_id='{0}'".format(id))
        return result['succeed']

    @staticmethod
    def convertToObj(queryTuple):
        stu = Student()
        stu.id = queryTuple[0]
        stu.name = queryTuple[1]
        stu.password = queryTuple[2]
        stu.gender = queryTuple[3]
        stu.is_delete = queryTuple[4]
        stu.age = queryTuple[5]
        stu.grade_id = queryTuple[6]
        stu.ins_id = queryTuple[7]
        return stu


class Application:
    def __init__(self):
        self.id = -1
        self.grade_id = -1
        self.stu_id = -1
        self.ins_id = -1
        self.time = 0
        self.reason_site = ''
        self.is_out = 0
        self.is_agreed = 0

    @staticmethod
    def getAll():
        queries = database.doQuery("select * from application")
        res = []
        for q in queries['data']:
            res.append(Application.convertToObj(q))
        return res

    @staticmethod
    def getAllWithDetail():
        res = []
        queries = database.doQuery("select * from application")
        for q in queries['data']:
            app = Application.convertToObj(q)
            grade = Grade.getById(app.grade_id)
            ins = Instructor.getById(app.ins_id)
            stu = Student.getById(app.stu_id)
            res.append({
                'id': app.id,
                'grade_id': app.grade_id,
                'stu_id': app.stu_id,
                'ins_id': app.ins_id,
                'time': app.time,
                'reason_site': app.reason_site,
                'is_out': app.is_out,
                'is_agreed': app.is_agreed,
                'grade': grade,
                'ins': ins,
                'stu': stu
            })
        return res

    @staticmethod
    def getAllWithDetailByStuId(id):
        res = []
        queries = database.doQuery("select * from application where app_stu_id='{0}'".format(id))
        for q in queries['data']:
            app = Application.convertToObj(q)
            grade = Grade.getById(app.grade_id)
            ins = Instructor.getById(app.ins_id)
            stu = Student.getById(app.stu_id)
            res.append({
                'id': app.id,
                'grade_id': app.grade_id,
                'stu_id': app.stu_id,
                'ins_id': app.ins_id,
                'time': app.time,
                'reason_site': app.reason_site,
                'is_out': app.is_out,
                'is_agreed': app.is_agreed,
                'grade': grade,
                'ins': ins,
                'stu': stu
            })
        return res

    @staticmethod
    def getById(id):
        app = None
        query = database.doQuery("select * from application where app_id='{0}'".format(id))
        if len(query['data']) > 0:
            app = Application.convertToObj(query['data'][0])
        return app

    @staticmethod
    def confirm(app_id, is_agreed):
        result = database.doUpdate("update application set app_is_agreed='{0}' where app_id='{1}'".format(is_agreed, app_id))
        print(result)
        return result['succeed']

    @staticmethod
    def insert(grade_id, stu_id, ins_id, time, reason_site, is_out):
        result = database.doQuery("select * from application where grade_id='{0}' and stu_id='{1}' and ins_id='{2}' and time='{3}'".format(grade_id, stu_id, ins_id, time))
        if result['succeed']:
            return False
        result = database.doInsert("insert into application values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', 0, 0)".format(grade_id, stu_id, ins_id, time, reason_site, is_out))
        return result['succeed']

    @staticmethod
    def delete(id):
        pass

    @staticmethod
    def convertToObj(queryTuple):
        app = Application()
        app.grade_id = queryTuple[0]
        app.stu_id = queryTuple[1]
        app.ins_id = queryTuple[2]
        app.time = queryTuple[3]
        app.reason_site = queryTuple[4]
        app.is_out = queryTuple[5]
        app.is_agreed = queryTuple[6]
        app.id = queryTuple[7]
        return app

