import pymysql

HOST = 'localhost'
USER = 'root'
PASSWORD = 'QQqq11.com'
DATABASE = 'db_school'
CHARSET = 'utf8'

def connect(): #def：定义一个函数
    db = pymysql.connect(    #连接数据库
            host=HOST, 
            user=USER,        #用户名
            password=PASSWORD, #密码
            database=DATABASE, 
            charset=CHARSET)   #要连接的数据库的字符编码
    return db

def close(db):
    db.close()   #关闭数据库的连接

def doQuery(sql):
    db = connect()
    result = dict()  #创建字典
    try:
        cursor = db.cursor()   #创建游标对象
        cursor.execute(sql)    #执行sql语句
        result['succeed'] = True  #字典中新增一个键值对
        result['data'] = cursor.fetchall()  #获取全部数据
    except Exception:
        result['succeed'] = False
        result['data'] = []
    finally:           #无论try中的语句是否有异常，finally中的语句一定会执行
        cursor.close()    #关闭当前游标
        close(db)         #关闭数据库的连接
        return result      #返回字典

def doInsert(sql):
    db = connect()
    result = dict()
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        result['succeed'] = True
    except Exception as e:
        result['succeed'] = False
    finally:
        cursor.close()
        close(db)
        return result

def doUpdate(sql):
    db = connect()
    result = dict()
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        result['succeed'] = True
    except Exception as e:
        print(e) #打印关于错误的信息
        result['succeed'] = False
    finally:
        cursor.close()
        close(db)
        return result

def doDelete(sql):
    db = connect()
    result = dict()
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()        #提交事务
        result['succeed'] = True
    except:
        result['succeed'] = False
    finally:
        cursor.close()
        close(db)
        return result
