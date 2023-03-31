from dbhelper import DBhelper

def main():
    db=DBhelper()
    while True:
        print("*********WELCOME*********\n")
        
        print("Enter Your Chose(1-5):\n")
        print("1: Insert New User.")
        print("2: Display All User.")
        print("3: Delete User.")
        print("4: Update User.")
        print("5: Exit.")
        try:
            choice=int(input())
            if(choice==1):
                print("sorry this time it is under devlapment\n")
                pass
            elif choice==2:
                db.fetch_all()
                pass
            elif choice==3:
                print("sorry this time it is under devlapment\n")
                pass
            elif choice==4:
                print("sorry this time it is under devlapment\n")
                pass
            elif choice==5:
                print("Program Exit\n")
                break
            else:
                print("Invalid input ! Try again")
        except Exception as e:
            print(e)
            print("Invalid input ! Try again")

if __name__=="__main__":
    main()
