import random as rd


user = "abhi"
info = {"abhi": "1234", "aku": "4567"}
users = ["abhi","aku"]
marks = {"abhi":[4,3,5],"aku":[None,3,None]}

qysPython = [
    ["When was Python first released?", "1991", "1995", "2000", "2005", "1991"],
    ["Who is the creator of Python?", "James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup", "Guido van Rossum"],
    ["What is the file extension for Python files?", ".py", ".java", ".class", ".js", ".py"],
    ["Which of these is not a Python data type?", "int", "float", "list", "char", "char"],
    ["What does PEP stand for in Python?", "Python Enhancement Proposal", "Python Execution Process", "Python Encrypted Program", "Python Event Procedure", "Python Enhancement Proposal"],
    ["Which company oversees Python?", "Oracle", "Microsoft", "Google", "Python Software Foundation", "Python Software Foundation"],
    ["What is the latest major version of Python (as of 2023)?", "Python 2", "Python 3", "Python 4", "Python 5", "Python 3"],
    ["Which keyword is used to define a function in Python?", "func", "function", "def", "declare", "def"],
    ["What is a correct syntax to output 'Hello World' in Python?", "print('Hello World')", "echo 'Hello World'", "Console.WriteLine('Hello World')", "printf('Hello World')", "print('Hello World')"],
    ["Which of these is used to handle exceptions in Python?", "try-except", "if-else", "for loop", "while loop", "try-except"],
    ["What type of programming language is Python?", "Functional", "Object-oriented", "Procedural", "All of the above", "All of the above"],
    ["What is the default value of 'None' in Python?", "Null", "False", "None", "Zero", "None"],
    ["Which of these is a mutable data type in Python?", "tuple", "int", "list", "str", "list"],
    ["How do you start a comment in Python?", "#", "//", "/*", "--", "#"],
    ["Which of these is a correct method to create a list in Python?", "list()", "List()", "createList()", "listNew()", "list()"],
    ["How do you declare a variable in Python?", "var x = 5", "let x = 5", "x = 5", "declare x = 5", "x = 5"],
    ["Which of the following is a Python framework for web development?", "Django", "React", "Angular", "Spring", "Django"],
    ["What does 'len()' function do in Python?", "Returns the length of a list or string", "Calculates sum", "Finds average", "Returns the type", "Returns the length of a list or string"],
    ["How do you create a dictionary in Python?", "{'key': 'value'}", "dict()", "Both", "None", "Both"],
    ["Which keyword is used to define a class in Python?", "class", "Class", "def", "define", "class"]
]

qysJava = [
    ["When was Java first released?", "1991", "1995", "2000", "2005", "1995"],
    ["Who is the creator of Java?", "James Gosling", "Guido van Rossum", "Bjarne Stroustrup", "Dennis Ritchie", "James Gosling"],
    ["What is the file extension for Java files?", ".java", ".class", ".jar", ".js", ".java"],
    ["Which of these is not a Java primitive data type?", "int", "float", "string", "char", "string"],
    ["What does JVM stand for?", "Java Variable Machine", "Java Virtual Machine", "Java Version Manager", "Java Visual Machine", "Java Virtual Machine"],
    ["Which company originally developed Java?", "Oracle", "Microsoft", "Google", "Sun Microsystems", "Sun Microsystems"],
    ["What does JDK stand for?", "Java Development Kit", "Java Deployment Kit", "Java Design Kit", "Java Debug Kit", "Java Development Kit"],
    ["Which keyword is used to inherit a class in Java?", "inherit", "extends", "implements", "override", "extends"],
    ["Which method is the entry point of a Java application?", "start()", "main()", "run()", "init()", "main()"],
    ["Which of these is used to handle exceptions in Java?", "try-catch", "if-else", "for loop", "while loop", "try-catch"],
    ["What is Java primarily known as?", "Functional language", "Object-oriented language", "Procedural language", "Logic programming language", "Object-oriented language"],
    ["Which of the following is not a valid access modifier in Java?", "public", "protected", "internal", "private", "internal"],
    ["What does 'static' mean in Java?", "Belongs to the class, not an instance", "Can be inherited", "Can be overridden", "None of the above", "Belongs to the class, not an instance"],
    ["Which of these is used for creating threads in Java?", "Thread class", "Runnable interface", "Both", "None of the above", "Both"],
    ["Which package contains the core classes in Java?", "java.awt", "java.lang", "java.util", "java.io", "java.lang"],
    ["How do you declare an array in Java?", "int arr[]", "int arr", "array int[]", "int[] array", "int arr[]"],
    ["Which of these is not a feature of Java?", "Platform-independent", "Automatic memory management", "Multiple inheritance of classes", "Object-oriented", "Multiple inheritance of classes"],
    ["Which version of Java introduced the 'lambda' feature?", "Java 5", "Java 7", "Java 8", "Java 9", "Java 8"],
    ["What is the default value of a boolean in Java?", "true", "false", "0", "1", "false"],
    ["Which keyword is used to prevent inheritance in Java?", "sealed", "final", "static", "const", "final"]
]

qysKotlin = [
    ["When was Kotlin launched?", "2004", "2016", "2017", "2018", "2016"],
    ["Which company developed Kotlin?", "Microsoft", "JetBrains", "Google", "Oracle", "JetBrains"],
    ["Is Kotlin statically or dynamically typed?", "Statically typed", "Dynamically typed", "Both", "Neither", "Statically typed"],
    ["What is the extension of Kotlin files?", ".kt", ".java", ".kotlin", ".class", ".kt"],
    ["Which language does Kotlin primarily interoperate with?", "C++", "Java", "Python", "Swift", "Java"],
    ["Which platform is Kotlin mainly used for?", "iOS", "Windows", "Android", "Linux", "Android"],
    ["What is the name of the tool Kotlin uses for managing dependencies?", "Gradle", "Maven", "Ant", "Make", "Gradle"],
    ["What does 'val' represent in Kotlin?", "Mutable variable", "Immutable variable", "Function", "Class", "Immutable variable"],
    ["Which of these is a Kotlin coroutine builder?", "launch", "async", "run", "suspend", "launch"],
    ["Which keyword is used in Kotlin to declare a function?", "def", "fun", "func", "function", "fun"],
    ["What is the primary programming paradigm of Kotlin?", "Object-oriented", "Functional", "Both", "Procedural", "Both"],
    ["How do you declare a nullable type in Kotlin?", "Type?", "nullable<Type>", "Type!", "optional<Type>", "Type?"],
    ["Which of the following is a higher-order function in Kotlin?", "forEach", "map", "filter", "All of the above", "All of the above"],
    ["What is the main difference between 'var' and 'val' in Kotlin?", "'var' is mutable and 'val' is immutable", "'val' is mutable and 'var' is immutable", "Both are immutable", "Both are mutable", "'var' is mutable and 'val' is immutable"],
    ["Which keyword is used to inherit a class in Kotlin?", "inherit", "extend", "super", "override", "extend"],
    ["How can you create a singleton in Kotlin?", "object", "class", "singleton", "static", "object"],
    ["What is the default visibility modifier in Kotlin?", "public", "private", "protected", "internal", "public"],
    ["Which of these is a valid way to declare a read-only variable in Kotlin?", "val x = 5", "let x = 5", "var x = 5", "x = 5", "val x = 5"],
    ["What is Kotlin's primary target JVM version?", "JVM 6", "JVM 7", "JVM 8", "JVM 9", "JVM 8"],
    ["Which Kotlin feature allows working with asynchronous programming?", "Lambdas", "Coroutines", "Generics", "Null safety", "Coroutines"]
]

def main():
    a=True
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

def register():
    un = input("Enter Username: ")
    if un not in users:
        pwd = input("Enter Password: ")
        users.append(un)
        info[un] = pwd
        marks[un] = [None]*3
        print("*-* User created successfully *-*")
        main()
    else:
        print("-- -- User already exists -- --")

def login(qolp=0,qoln=0):
    global user
    un = input("Enter your username: ")
    if un in users:
        pwd = input("Enter Password: ")
        if pwd == info[un]:
            print("*-* Welcome *-*")
            user = un
            langChoose()
        else:
            print("-- -- Wrong Password -- --")
            if qolp >= 2:
                print("-- -- You have tried maximum time -- -- \n -- -- Please Start from Beginning -- --")
                main()
            qolp+=1
            login(qolp=qolp,qoln=qoln)
    else:
        print("-- -- User does not exist -- --")
        if qoln >= 2:
            print("-- -- You have tried maximum time -- -- \n -- -- Please Start from Beginning -- --")
            main()
        qoln+=1
        login(qolp=qolp,qoln=qoln)

def langChoose():
    global user
    print(f"Choose your language {user}: \n 1. Python \n 2. Java \n 3. Kotlin \n 4. Marks \n 5. Logout")
    choice = input("Enter your choice: ")
    if choice == "1":
        lang("Python",qysPython)
    elif choice == "2":
        lang("Java",qysJava)
    elif choice == "3":
        lang("Kotlin",qysKotlin)
    elif choice == "4":
        print(f"Your marks- \n Kotlin: {marks[user][2]} \n Python: {marks[user][0]} \n Java: {marks[user][1]}")
        langChoose()
    elif choice == "5":
        main()
    else:
        print("no other languages available")
        langChoose()

def rng():
    i=0
    r=[]
    while i<5:
        t=rd.randint(0,19)
        if t not in r:
            r.append(t)
            i+=1
    return r

def lang(name,qys):
    result = Quiz(qys,name)
    assignmarks(result,name)
    afterquiz(name)

def Quiz(qys,lang):
    qs = rng()
    q = 1
    correct = 0
    print(f"*-* You are attempting {lang} Quiz *-*")
    for i in qs:
        print(f"{q}) {qys[i][0]}")
        q += 1
        for j in range(1, 5):
            print(f"{j} -> {qys[i][j]}")
        ans = int(input("Enter your choice: "))
        while ans not in range(1,5):
            print("Invalid choice")
        else:
            if qys[i][ans] == qys[i][5]:
                correct += 1
    return correct

def assignmarks(mk,lang):
    if lang == "Python":
        if marks[user][0] is None:
            marks[user][0] = mk
        else:
            if marks[user][0] < mk:
                marks[user][0] = mk
    elif lang == "Java":
        if marks[user][1] is None:
            marks[user][1] = mk
        else:
            if marks[user][1] < mk:
                marks[user][1] = mk
    elif lang == "Kotlin":
        if marks[user][2] is None:
            marks[user][2] = mk
        else:
            if marks[user][2] < mk:
                marks[user][2] = mk
    print(f"You scored {mk} out of 5")

def afterquiz(name):
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


if __name__ == '__main__':
    main()