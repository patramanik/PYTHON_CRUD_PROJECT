import mysql.connector as connector


class DBhelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                  port='3306',
                  user='root',
                  password='',
                  database='py_db'
                  )
        query='create table if not exists user(userId int primary key,Uname varchar(200),phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print("\nTable Created\n")

    #Insert into table
    def insert_user(self,userid,uname,phone):
        query="insert into user(userId,uname,phone) values('{}','{}','{}')".format(userid,uname,phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user seved to db")
    #fech All
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id : ",row[0])
            print("User Name : ",row[1])
            print("User Phone : ",row[2])
            print()
            print()
    #fatch one
    def fatch_one(self,UserId):
        query="select * from user where userId={}".format(UserId)
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id : ",row[0])
            print("User Name : ",row[1])
            print("User Phone : ",row[2])
            print()
    
    # delet User
    def delete_user(self,UserId):
        query="delete from user where userId='{}'".format(UserId)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print(UserId," deleted\n")
    
    # Updet user  
    def updet_user(self,UserId,newName,newPhone):
        query="update user set Uname='{}',phone='{}' where userId={}".format(newName,newPhone,UserId)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print(UserId," Updeted Done\n")

        






# main coding
helper=DBhelper()
# helper.insert_user(1,'Manik Patra',8158021116)
# helper.insert_user(6,'Arko Shamonta',8159200438)
# helper.fetch_all()
# input=input("Enter User Id : ")
# helper.fatch_one(input)
# helper.delete_user(input)
# helper.updet_user(6,'Arko Prava Shamanta',8918327205)


