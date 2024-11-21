import random as rd
import datetime as dt
import mysql.connector as sql

'''info -> uid, username, email, password
questions -> qno,lang,question,1,2,3,4,answer
quiz history -> qzno, uid, lang, marks, time
marks -> uid, python, java, kotlin'''

user = "avi6"

qysPython = []
qysKotlin = []
qysJava = []

db = sql.connect(host="localhost", user="root", passwd="abhi", database="quiz")

# Main function
def main():
    global users,marks,info,contact
    a=True
    print("*-* Welcome to Quiz App *-*")
    while a:
        print("Enter the choice: \n 1. Register \n 2. Login \n 3. Quiz \n 4. Add Question \n 5. Quit")
        choice = input("Your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            if user != "":
                langChoose()
            else:
                print("-- -- Please login first -- --")
        elif choice == "4":
            addques()
        elif choice == "5":
            print("-- -- Thank you -- --")
            break
        else:
            print("Invalid choice")

def bringQuestions(name):  # getting question for the quiz
    cur = db.cursor()
    cur.execute("Select questions,option_a,option_b,option_c,option_d,answer from questions where lang = %s",(name,))
    qys = cur.fetchall()
    return qys

def addques():  #will be used to add one question at a time
    lang = input("Enter your question's language: ")
    if lang.lower() in ("python","java","kotlin"):
        q = input("Enter your question")
        a = input("Enter 1st option: ")
        b = input("Enter 2nd option: ")
        c = input("Enter 3rd option: ")
        d = input("Enter 4th option: ")
        ans = input("Enter answer: ")
        if ans in (a,b,c,d):
            cur = db.cursor()
            cur.execute("Insert into questions(lang,questions,option_a,option_b,option_c,option_d,answer) values(%s,%s,%s,%s,%s,%s,%s)",(lang,q,a,b,c,d,ans))
            db.commit()
        else:
            print("Invalid answer, Please try again")
            addques()
    else:
        print("Unavailable Language")
        main()

def rng():  # Giving the random numbers list to display randomly choosen question
    i=0
    r=[]
    while i<5:
        t=rd.randint(0,19)
        if t not in r:
            r.append(t)
            i+=1
    return r

def register():  # Registering user
    name = input("Enter your username: ")
    cur = db.cursor()
    cur.execute("SELECT uid FROM info WHERE username = %s",(name,))
    id = cur.fetchone()
    if id is not None:
        print("Username already exists")
        main()
    email = input("Enter your email: ")
    pwd = input("Enter Password: ")
    cur.execute("INSERT INTO info(username,email,password) values(%s,%s,%s)",(name,email,pwd))
    db.commit()
    cur.execute("SELECT uid FROM info WHERE username = %s",(name,))
    ud = cur.fetchone()
    cur.execute("INSERT INTO marks values(%s,0,0,0)",(ud))
    db.commit()
    print("*-* User created successfully *-*")
    main()

def login(qolp=0,qoln=0):  #Logging in user
    global user
    un = input("Enter your username: ")
    cur = db.cursor()
    cur.execute("SELECT password FROM info WHERE username = %s",(un,))
    psd = cur.fetchone()
    if psd is not None:
        pwd = input("Enter Password: ")
        if pwd == psd[0]:
            print("*-* Welcome *-*")
            user = un
            langChoose()
        else:
            print("-- -- Wrong Password -- --")
            if qolp >= 2:
                print("-- -- You have tried maximum time -- --")
                Forget()
            qolp+=1
            login(qolp=qolp,qoln=qoln)
    else:
        print("-- -- User does not exist -- --")
        if qoln >= 2:

            print("-- -- You have tried maximum time -- --")
            Forget()
        qoln+=1
        login(qolp=qolp,qoln=qoln)

def langChoose():  # Giving choice to pick language, show marks and history, logout
    global user,qysPython,qysKotlin,qysJava
    print(f"Choose your language {user}: \n 1. Python \n 2. Java \n 3. Kotlin \n 4. Marks \n 5. History \n "
          f"6. Logout")
    choice = input("Enter your choice: ")
    if choice == "1":
        if not qysPython:
            qysPython = bringQuestions("python")
        lang("Python",qysPython)
    elif choice == "2":
        if not qysJava:
            qysJava = bringQuestions("java")
        lang("Java",qysJava)
    elif choice == "3":
        if not qysKotlin:
            qysKotlin = bringQuestions("kotlin")
        lang("Kotlin",qysKotlin)
    elif choice == "4":
        cur = db.cursor()
        cur.execute("SELECT pymarks,ktmarks,javamarks from marks where uid = (Select uid from info where username = %s)",(user,))
        marks = cur.fetchone()
        print(f"Your marks- \n Kotlin: {marks[1]} \n Python: {marks[0]} \n Java: {marks[2]}")
        langChoose()
    elif choice == "5":
        cur = db.cursor()
        cur.execute("SELECT lang,marks,time from quiz where uid = (Select uid from info where username = %s)",(user,))
        history = cur.fetchall()
        if len(history) == 0:
            print("-- -- No history -- --")
        else:
            print("Language | Marks |   date and time")
        for i in history:
            if len(i)==1:
                pass
            else:
                print(f"{i[0].center(8)} | {str(i[1]).center(5)} | {i[2]}")
        input("Press Enter to continue")
        langChoose()

    elif choice == "6":
        main()
    else:
        print("Invalid")
        langChoose()

def lang(name,qys):  # calling functions to execute the quiz of the choosen language
    result = Quiz(qys,name)
    assignmarks(result,name)
    afterquiz(name)

def Quiz(qys,lang):  # quiz
    qs = rng()
    q = 1
    option = [1,2,3,4]
    correct = 0
    print(f"*-* You are attempting {lang} Quiz *-*")
    for i in qs:
        rd.shuffle(option)
        o=0
        print(f"{q}) {qys[i][0]}")
        q += 1
        for j in option:
            print(f"{o+1} -> {qys[i][j]}",end="  ")
            o+=1
        ans = int(input("\nEnter your choice: "))
        while ans not in range(1,5):
            print("Invalid choice")
            ans = int(input("Enter your choice again: "))
        else:
            answer = option[ans-1]
            if qys[i][answer] == qys[i][5]:
                correct += 1
    return correct

def assignmarks(mk,lang):  #marks assignments
    global user
    if lang == "Python":
        cur = db.cursor()
        cur.execute("SELECT pymarks from marks where uid = (Select uid from info where username = %s)",(user,))
        mark = cur.fetchone()
        if mark[0] < mk:
            cur.execute("UPDATE marks set pymarks = %s where uid = (Select uid from info where username = %s)",(mk,user))
            db.commit()
    elif lang == "Java":
        cur = db.cursor()
        cur.execute("SELECT javamarks from marks where uid = (Select uid from info where username = %s)", (user,))
        mark = cur.fetchone()
        if mark[0] < mk:
            cur.execute("UPDATE marks set javamarks = %s where uid = (Select uid from info where username = %s)",
                        (mk, user))
            db.commit()
    elif lang == "Kotlin":
        cur = db.cursor()
        cur.execute("SELECT ktmarks from marks where uid = (Select uid from info where username = %s)", (user,))
        mark = cur.fetchone()
        if mark[0] < mk:
            cur.execute("UPDATE marks set ktmarks = %s where uid = (Select uid from info where username = %s)",
                        (mk, user))
            db.commit()
    time = dt.datetime.now().strftime("%H:%M %d-%m-%Y")
    cur = db.cursor()
    cur.execute("SELECT uid from info where username = %s",(user,))
    uid = cur.fetchone()
    id = uid[0]
    cur.execute("INSERT INTO quiz(uid,lang,marks,time) values (%s,%s,%s,%s)",(id,lang.lower(),mk,time))
    db.commit()
    print(f"You scored {mk} out of 5")

def afterquiz(name):  # dealing with what happens after quiz like retry, choose other language, etc
    print("What do you want to do now? \n 1. Retry \n 2. Choose different language and see all languages scores \n 3. Logout \n 4. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        if name == "Python":
            lang(name,qysPython)
        elif name == "Java":
            lang(name,qysJava)
        elif name == "Kotlin":
            lang(name,qysKotlin)
    if choice == "2":
        langChoose()
    if choice == "3":
        main()
    if choice == "4":
        print("bye")

# Extras
def Forget():
    global user
    print("1. Forgot Username \n2. Forgot Password \n3. Both \n4. Go back")
    choice = input("Enter your choice: ")
    if choice == "1":
        con = input("Enter your email: ")
        cur = db.cursor()
        cur.execute("SELECT username FROM info where email = %s",(con,))
        un = cur.fetchone()
        if un is not None:
            print(f"Your username is: {un[0]}")
        else:
            print("Invalid email")
            Forget()
        input("Press Enter to continue")
        main()
    elif choice == "2":
        usc = input("Enter your username or contact: ")
        cur = db.cursor()
        cur.execute("SELECT password FROM info where email = %s or username=%s", (usc,usc))
        pswd = cur.fetchone()
        if pswd is not None:
            print(f"Your password is: {pswd[0]}")
        else:
            print("Invalid username")
            Forget()
        input("Press Enter to continue")
        main()
    elif choice == "3":
        print("We cant help you")
        quit()
    elif choice == "4":
        main()

if __name__ == '__main__':
    main()
