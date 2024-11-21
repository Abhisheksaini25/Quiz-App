import random as rd
import datetime as dt
import math as m

# data/Subjects/Python <- path

user = "avi6"
info = {}
users = []
marks = {}
contact = []

qysPython = []
qysKotlin = []
qysJava = []

# Main function
def main():
    global users,marks,info,contact
    a=True
    users = getuser()
    marks = getmarks()
    info = getinfo()
    contact = getcontact()
    print("*-* Welcome to Quiz App *-*")
    while a:
        print("Enter the choice: \n 1. Register \n 2. Login \n 3. Quiz \n 4. Quit")
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
            print("-- -- Thank you -- --")
            break
        else:
            print("Invalid choice")

# One type to another type
def strtols(s):  #returns list of string
    sls = s.split('\n')
    return sls

def strtolist(s):  #returns list of list
    sls = s.split('\n')
    slist = []
    for i in sls:
        slist.append(i.split(','))
    return slist

# Getting information from files
def getuser():  #getting all the users registered
    with open('data/users', 'r') as userfile:
        userdata = userfile.read()
    return strtols(userdata)

def getinfo():  #getting all the info of user
    with open('data/info', 'r') as infofile:
        infodata = infofile.read()
        infols = infodata.split('\n')
    infolist = []
    for i in infols:
        infolist.append(i.split(','))
    infodict = {}
    for i in infolist:
        infodict[i[0]] = [i[1],i[2],i[3]]
    return infodict

def gethistory(user):  # getting user history
    with open(f'data/Historybyuser/{user}', 'r') as userhistory:
        history = userhistory.read()
    return strtolist(history)

def getcontact():  #getting all contact
    with open('data/contacts', 'r') as contactfile:
        contactdata = contactfile.read()
    return strtols(contactdata)

def getmarks():  # getting highest mark in each subject
    with open(f'data/mark', 'r') as markfile:
        markdata = markfile.read()
        markls = markdata.split('\n')
    marklist =[]
    for i in markls:
        marklist.append(i.split(','))
    markdict = {}
    for i in marklist:
        markdict[i[0]] = [i[1],i[2],i[3]]
    return markdict

def getallhistory():  # getting all history
    with open('data/history','r') as historyfile:
        historydata = historyfile.read()
        historyls = historydata.split('\n')
    historylist = []
    for i in historyls:
        historylist.append(i.split(','))
    return historylist

def bringQuestions(name):  # getting question for the quiz
    qys = []
    QuesFile = open(f"data/Subjects/{name}","r")
    Quesdata = QuesFile.read()
    Ques = Quesdata.split('\n')

    for i in Ques:
        qys.append(i.split(','))

    return qys

# Performing operation on files (adding,deleting,creating)
def postdata(add,data):  # posting all different datas in the data folder like contact, info, mark, users
    data = "\n"+data
    with open(f'data/{add}','a') as datafile:
        datafile.write(data)

def addques(add,que):  #will be used to add one question at a time
    que = "\n"+que
    with open(f'data/Subjects/{add}','a') as subsfile:
        subsfile.write(que)

def createhistory(user):  #creating user history in the file
    with open(f'data/Historybyuser/{user}', 'a') as history:
        history.write('')

def addhistory(user,sub,mark):  # Adding a new data in the history both all and user
    with open(f'data/Historybyuser/{user}','a') as history:
        history.write(f'{sub},{mark},{dt.datetime.now().strftime("%d-%b-%Y %H:%M")}\n')
    with open('data/history','a') as allhistory:
        allhistory.write(f'{user},{sub},{mark},{dt.datetime.now().strftime("%d-%b-%Y %H:%M")}\n')

def altermarks():  #updating new marks in the file
    global marks
    markstr = ''
    for i in marks:
        markstr += i+','+marks[i][0]+','+marks[i][1]+','+marks[i][2]+'\n'
    markstr = markstr[:-1]
    with open("data/mark", "w") as marksfile:
        marksfile.write(markstr)

# Giving some functionalities
def usernamecreator(name):  # Creating username
    global users
    username = ''
    while (not username) or (username in users):
        num = rd.randint(1*len(name),int(m.pow(2,len(name))))
        username = name + str(num)
    return username

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
    global contact,users
    name = input("Enter your name: ")
    con = input("Enter your contact number: ")
    if con in contact:
        print("Sorry you are already registered")
        main()
    pwd = input("Enter Password: ")
    un = usernamecreator(name)
    postdata("contacts",con)
    postdata("users",un)
    postdata("info",f"{un},{name},{con},{pwd}")
    postdata("mark",f"{un},0,0,0")
    createhistory(un)
    users = getuser()
    print("*-* User created successfully *-*")
    print("Your username is: ", un)
    main()

def login(qolp=0,qoln=0):  #Logging in user
    global user,users,info
    un = input("Enter your username: ")
    if un in users:
        pwd = input("Enter Password: ")
        if pwd == info[un][-1]:
            print("*-* Welcome *-*")
            user = un
            langChoose()
        else:
            print("-- -- Wrong Password -- --")
            if qolp >= 2:
                Forget()
                #print("-- -- You have tried maximum time -- -- \n -- -- Please Start from Beginning -- --")
                main()
            qolp+=1
            login(qolp=qolp,qoln=qoln)
    else:
        print("-- -- User does not exist -- --")
        if qoln >= 2:
            Forget()
            #print("-- -- You have tried maximum time -- -- \n -- -- Please Start from Beginning -- --")
            main()
        qoln+=1
        login(qolp=qolp,qoln=qoln)

def langChoose():  # Giving choice to pick language, show marks and history, logout
    global user,qysPython,qysJava,qysKotlin,info,marks
    print(f"Choose your language {info[user][0]}: \n 1. Python \n 2. Java \n 3. Kotlin \n 4. Marks \n 5. History \n "
          f"6. Logout")
    choice = input("Enter your choice: ")
    if choice == "1":
        if not qysPython:
            qysPython = bringQuestions("Python")
        lang("Python",qysPython)
    elif choice == "2":
        if not qysJava:
            qysJava = bringQuestions("Java")
        lang("Java",qysJava)
    elif choice == "3":
        if not qysKotlin:
            qysKotlin = bringQuestions("Kotlin")
        lang("Kotlin",qysKotlin)
    elif choice == "4":
        print(f"Your marks- \n Kotlin: {marks[user][2]} \n Python: {marks[user][0]} \n Java: {marks[user][1]}")
        langChoose()
    elif choice == "5":
        history = gethistory(user)
        print("Language | Marks |   date and time")
        for i in history:
            if len(i)==1:
                pass
            else:
                print(f"{i[0].center(8)} | {i[1].center(5)} | {i[2]}")
        input("Press Enter to continue")
        langChoose()

    elif choice == "6":
        main()
    else:
        print("no other options available")
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
    if lang == "Python":
        if marks[user][0] == "0":
            marks[user][0] = str(mk)
            altermarks()
        else:
            if int(marks[user][0]) < mk:
                marks[user][0] = str(mk)
                altermarks()
    elif lang == "Java":
        if marks[user][1] == "0":
            marks[user][1] = str(mk)
            altermarks()
        else:
            if int(marks[user][1]) < mk:
                marks[user][1] = str(mk)
                altermarks()
    elif lang == "Kotlin":
        if marks[user][2] == "0":
            marks[user][2] = str(mk)
            altermarks()
        else:
            if int(marks[user][2]) < mk:
                marks[user][2] = str(mk)
                altermarks()
    addhistory(user,lang,mk)
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
    global users,contact,info
    print("1. Forgot Username \n2. Forgot Password \n3. Both \n4. Go back")
    choice = input("Enter your choice: ")
    if choice == "1":
        con = input("Enter your contact no: ")
        if con in contact:
            for i in info:
                if info[i][1] == con:
                    print(f"Your username is: {i}")
                    break
        else:
            print("Invalid contact no")
            main()
        input("Press Enter to continue")
        main()
    elif choice == "2":
        usc = input("Enter your username or contact: ")
        if usc in users:
            print(f"Your password is: {info[usc][2]}")
        elif usc in contact:
            for i in info:
                if info[i][1] == usc:
                    print(f"Your password is: {info[i][2]}")
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
