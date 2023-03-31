from dbhelper import DBhelper

def main():
    db=DBhelper()
    while True:
        print("*********WELCOME*********\n")
        
        print("Enter Your Chose(1-6):\n")
        print("1: Insert New User.")
        print("2: Display All User.")
        print("3: Display one User.")
        print("4: Delete User.")
        print("5: Update User.")
        print("6: Exit.")
        try:
            choice=int(input("Enter your chose: "))
            if(choice==1):
                uid=input("Enter UserId: ")
                UserName=input("Enter UserName: ")
                UserPhone=input("Enter phone: ")
                db.insert_user(uid,UserName,UserPhone)
                pass
            elif choice==2:
                db.fetch_all()
            elif choice==3:
                uid=input("Enter UserId: ")
                print()
                db.fatch_one(uid)
            elif choice==4:
                uid=input("Enter UserId: ")
                db.delete_user(uid)
            elif choice==5:
                uid=input("Enter UserId: ")
                User_newName=input("Enter NewName: ")
                User_newPhone=input("Enter Newphone: ")
                db.updet_user(uid,User_newName,User_newPhone)
                pass
            elif choice==6:
                print("Program Exit\n")
                break
            else:
                print("Invalid input ! Try again")
        except Exception as e:
            print(e)
            print("Invalid input ! Try again")

if __name__=="__main__":
    main()
