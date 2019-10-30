from StudentMysql import StuMysql
import json

class User1:
    def __init__(self,loginName,loginPwd):
        self.sql=StuMysql(loginName,loginPwd)
        self.tbName=self.IO_sql()
        self.menu()
    def menu(self):
        print("用户注册管理系统")
        print("\t 1.查找/修改/删除用户信息")
        print("\t 2.创建新数据库")
        print("\t 3.创建新用户")
        print("\t 4.查看所有用户")
        print("\t 5.退出系统")
        action = input("请输入序号选择对应菜单：")
        if action == '1':
            pass
            # self.updataUser()
        elif action == "2":
            self.Create_db()
        elif action=="3":
            self.CreateUser()
        elif action == "4":
            self.showAll()
        else:
            "系统已推出"

    def showAll(self):
        index=self.sql.execute(self.sql.SelectAllUser(self.tbName))
        print("index:",index)
        print("indexType:",type(index))
        print(len(index))
        print(index is None)
        if len(index)==0:
            print("当前无用户注册")
        else:
            for x in index:
                print("编号：{}\t姓名：{}\t".format(x[0], x[1]))
        self.menu()

    def Create_db(self):
        dbName=input("请输入新数据库名：")
        tbName=input("请输入新数据表名：")
        self.sql.Create_db(dbName,tbName)
        local_dbNameDict={"{}".format(dbName):"{}".format(tbName)}
        try:
            with open("./data/db.json", "a+", encoding="utf-8") as f:
                content=json.load(f)
                sql_list=content.get("sql")
                sql_list.append(local_dbNameDict)
                content["sql"]=sql_list
                json.dump(content,f)
            print("创建成功")
            self.IO_sql()
            self.menu()
        except json.decoder.JSONDecodeError:
            sql_list = []
            sql_list.append(local_dbNameDict)
            content={"sql":sql_list}
            with open("./data/db.json", "a+", encoding="utf-8") as f:
                json.dump(content,f)
                print("创建成功")
            self.menu()
    def CreateUser(self):
        name=input("请输入用户名：")
        pwd=input("请输入用户密码：")
        print("self.tbName:",self.tbName)
        if self.sql.Find_stu(self.tbName,name):
            print("该用户已存在")
        else:
            self.sql.Create_User(self.tbName,name, pwd)
            print("保存成功")
        self.menu()

    def IO_sql(self):
        try:
            with open("./data/db.json",mode="r+",encoding="utf-8") as f:
                dbContent=json.load(f)
                print(type(dbContent))
                print(dbContent is None)
                if dbContent is None:
                    print("当前没有创建数据库")
                    self.menu()
                else :
                    sql_list=dbContent.get("sql")
                    if len(sql_list):
                        self.dbNamelist=sql_list[-1]
                        self.dbNameItems=list(self.dbNamelist.items())[0]
                        self.dbNameKey=self.dbNameItems[0]
                        print("self.dbNameKey:",self.dbNameKey)
                        self.sql.execute("use {}".format(self.dbNameKey))
                        self.tbName=self.dbNameItems[1]
                    else:
                        self.tbName="student"
            print("self.tbName",self.tbName)
            return self.tbName
        except FileNotFoundError:
            print("当前没有创建数据库，需先创建数据库")
            self.menu()
        except json.decoder.JSONDecodeError:
            print("当前没有创建数据库，需先创建数据库")
            self.menu()


