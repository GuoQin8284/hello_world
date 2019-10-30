import pymysql

class StuMysql:



    # 创建数据库链接对象
    def __init__(self,name,pwd):
        self.cn1=pymysql.connect("127.0.0.1",name,pwd)
        self.cursor=self.cn1.cursor()

    # 执行sql命令方法
    def execute(self,sql):
        self.cursor.execute(sql)
        self.cn1.commit()
        a=self.cursor.fetchall()
        print("a:",a)
        return a

    # 输出查询信息
    def PrintInfo(self,select_sql):
        print(self.execute(select_sql))

    def SelectAllUser(self,tbName):
        self.selectAllUser="select * from {}".format(tbName)
        return self.selectAllUser

    def Create_db(self,dbName,tbName):
        self.create_db = "create database if not exists {} character set utf8".format(dbName)
        self.create_table="create table {}(id int unsigned primary key auto_increment,name varchar(5),pwd varchar(10))".format(tbName)
        self.use_db="use {}".format(dbName)
        self.execute(self.create_db)
        self.execute(self.use_db)
        self.execute(self.create_table)
        # return self.create_db

    def UpdateUserInfo(self,oldName,newName,tbName):
        self.updateUser="update {} set name={} where name={}".format(newName,oldName,tbName)
        return self.updateUser

    def SelectUser(self,tbName,name):
        self.selectUser="select * from {} where name='{}'".format(tbName,name)
        return self.execute(self.selectUser)

    def DeleteUser(self,tbName,name):
        self.deleteUser="delete from {} where name={}".format(tbName,name)
        return self.deleteUser

    def Find_stu(self,tbName,name):
        if len(self.SelectUser(tbName,name)):
            print("len(self.SelectUser(tbName,name):", len(self.SelectUser(tbName, name)))
            return 1
        else:
            return 0

    def Create_User(self,tbName,name,pwd):
        createUesr = "insert into {} values (null,'{}','{}')".format(tbName,name,pwd)
        print("createUesr:",createUesr)
        self.execute(createUesr)
