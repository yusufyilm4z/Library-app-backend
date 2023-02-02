import time
def menu():
    print('''
    \n------------------------------------------------------------------------------
    Enter "1" to list all the books
    Enter "2" to list all the books that are checked out
    Enter "3" to add a new book
    Enter "4" to search a book by ISBN number
    Enter "5" to search a book by name
    Enter "6" to check out a book to a student
    Enter "0" to exit the app 
------------------------------------------------------------------------------
    ''')

#1st function
def listAllBooks(books):
    time.sleep(0.5)
    print("Please wait...\n")
    time.sleep(0.7)
    print("-------------------------------------------------------------------------")
    for book in books:
        if len(book)>1:
            print("-->  "+book)
    print("-------------------------------------------------------------------------\n")

#2nd function
def checkedBooks():
    f = open("books.txt","r", errors="ignore")
    file = f.readlines()
    f.close()
    for line in file:
        if len(line)>1: #skiped the blank lines
            line=line.replace(" ","*")
            line = line.replace(","," ")
            line = line.split()
            #print(line)
            if line[-1]=="True":
                line.remove("True")
                line.append("{CHECKED OUT}")
                line = ",".join(idx[0:] for idx in line)
                line=line.replace("*"," ")
                line = line.split(",")
                line1 = line.pop(1)
                line2 = line.pop(-1)
                print("--> "+line1+" "+line2)
    f.close()

#3rd function
def checkisbn(d,list):
    isbnInput=input("Please enter 10 digit ISBN number of the book: ")
    if len(isbnInput)==10:
        if isbnInput not in d.keys():
            list.append(isbnInput)
            bookname=input("Enter the book name: ")
            list.append(bookname)
            authorName=input("Enter the author name: ")
            list.append(authorName)
            list.append("False")
        else:
            while isbnInput in d.keys():
                print("ERROR!: We already have that book.\n")
                isbnInput=input("Please enter again! ISBN number: ")

                if isbnInput not in d.keys() and len(isbnInput)==10:
                    list.append(isbnInput)
                    bookname=input("Enter the book name: ")
                    list.append(bookname)
                    authorName=input("Enter the author name: ")
                    list.append(authorName)
                    list.append("False")
                else:
                    while isbnInput not in d.keys() and len(isbnInput)!=10:
                        print("ERROR!: Please make sure enter 10 digit\n")
                        isbnInput=input("Please enter again! ISBN number: ")

                        if isbnInput not in d.keys() and len(isbnInput)==10:
                            list.append(isbnInput)
                            bookname=input("Enter the book name: ")
                            list.append(bookname)
                            authorName=input("Enter the author name: ")
                            list.append(authorName)
                            list.append("False")
    else:
        while len(isbnInput)!=10:
            print("ERROR!: Please make sure enter 10 digit\n")
            isbnInput=input("Please enter again! ISBN number: ")

            if len(isbnInput)==10:
                    if isbnInput not in d.keys():
                        list.append(isbnInput)
                        bookname=input("Enter the book name: ")
                        list.append(bookname)
                        authorName=input("Enter the author name: ")
                        list.append(authorName)
                        list.append("False")
                    else:
                        while isbnInput in d.keys():
                            print("ERROR!: We already have that book.\n")
                            isbnInput=input("Please enter again! ISBN number: ")

                            if isbnInput not in d.keys() and len(isbnInput)==10:
                                list.append(isbnInput)
                                bookname=input("Enter the book name: ")
                                list.append(bookname)
                                authorName=input("Enter the author name: ")
                                list.append(authorName)
                                list.append("False")

                            else:
                                while isbnInput not in d.keys() and len(isbnInput)!=10:
                                    print("ERROR!: Please make sure enter 10 digit\n")
                                    isbnInput=input("Please enter again! ISBN number: ")

                                    if isbnInput not in d.keys() and len(isbnInput)==10:
                                        list.append(isbnInput)
                                        bookname=input("Enter the book name: ")
                                        list.append(bookname)
                                        authorName=input("Enter the author name: ")
                                        list.append(authorName)
                                        list.append("False")
#4th function
def addNewBook(): #txt dosyasının sonunda en az bir satır boş değilse yanlış yazıyor.
    f= open("books.txt", "r")
    file=f.readlines()
    f.close()
    list=[]

    tupleList=[]
    for line in file:
        if len(line)>1:
            tempLine=line
            line=line.replace(","," ")
            line=line.split()
            tupleList.append((line[0],tempLine))
    d=dict(tupleList)
    checkisbn(d,list)
    isbnInput=list[0]
    list=",".join(idx[0:] for idx in list)
    d[isbnInput]=list
    #print(d.values())
    valueList=[]
    for i in d.values():
        valueList.append(i)
    #print(valueList)
    valueList[-1] = valueList[-1]+"\n"
    g=open("books.txt","a")
    g.write(valueList[-1])
    g.close()

    print("\nYou added a new book to the library.")
    print("\nReturning to menu please wait...")
    time.sleep(2.5)

#5th function
def findByISBN():
    f = open("books.txt","r")
    lineInfo = f.readlines()
    f.close()
    isbnNumbers=[]
    for line in lineInfo:
        if len(line)>1:
            line = line.replace(","," ")
            line = line.split()
            isbnNumber=line[0]
            isbnNumbers.append(isbnNumber)
    #print(isbnNumbers)
    #print(lineInfo)
    d=dict(zip(isbnNumbers, lineInfo))
    #print(d)
    isbnInput=input("Enter the ISBN number of the book you want to find: ")
    print("Searching in the library.") 
    time.sleep(0.75)
    print("Searching in the library..")
    time.sleep(0.75)
    print("Searching in the library...")
    time.sleep(0.75)
    if isbnInput not in isbnNumbers:
        print("\nHere is your result: ")
        print("\nSorry, there is no book have that ISBN number.")
    for i in d.keys():
        if i==isbnInput:
            print("\nHere is your result: ")
            print("\n--> "+d.get(i))

#6th function
def searchBookbyName(): #Bir kitapbın içerisinden aynı kelime iki defa geçerse ikidefa yazdırıyor
    f=open("books.txt","r")
    file = f.readlines()
    f.close()
    bookList=[]
    for line in file:
        line = line.replace(","," ")
        #line = line.split()
        bookList.append(line)
    #print(bookList)
    d=dict(zip(bookList,file))
    searchBox=input("Enter the name of the book or a word in the name: ")
    
    print("Searching in the library...")
    time.sleep(1.0)
    searchBox=searchBox.upper()
    if searchBox not in d.keys():
        print("\nHere is your result: ")
    count=0
    for key in d.keys():
        a = key
        key = key.split()
        for word in key:
            if word.upper() == searchBox:
                print("\n--> "+d.get(a))
                count+=1
    if count==1:
        print("We found '{}' book that contain this word.".format(count))
    elif count>1:
        print("We found '{}' books that contain this word.".format(count))

#7th function
def userLogin():
    f = open("students.txt","r", errors="ignore")
    lines = f.readlines()
    f.close()
    userIDs=[]
    for line in lines:
        if len(line)>1:
            line = line.split()
            userIDs.append(line[0])
    #print(userIDs)
    userNames=[]
    for line in lines:
        line=line.split()
        userName=line[1]+" "+line[2]
        userNames.append(userName)
    #print(userNames)
    d=dict(zip(userIDs,userNames))
    #print(d)
    userLoginInput = input("\nPlease enter your student ID: ")
    while userLoginInput not in d.keys():
        print("Invalid user ID, please try again.\n")
        userLoginInput = input("Please enter your student ID: ")
    print("Login successful. Hi! {}".format(d.get(userLoginInput)))
    return d.get(userLoginInput)
#8th
def checkoutBook():
    g = open("books.txt","r")
    lines=g.readlines()
    g.close()
    isbnNumbers=[]
    for line in lines:
        if len(line)>1:
            line = line.replace(","," ")
            line = line.split()
            isbnNumbers.append(line[0])
    #print(isbnNumbers)
    c=dict(zip(isbnNumbers,lines))
    chooseAbook=input("\nEnter the ISBN number of book you want to check out: ")
    while chooseAbook not in isbnNumbers:
        print("Invalid ISBN number, please try again.\n")
        chooseAbook=input("Enter the ISBN number of book you want to check out: ")
    for isbnNumber in c.keys():
        if isbnNumber==chooseAbook:
            temp = str(c.get(isbnNumber))
            tempOftemp=temp
            temp=temp.replace(" ","*")
            temp=temp.replace(","," ")
            temp=temp.split()
            temp[-1]="True"
            temp=",".join(index[0:] for index in temp)
            temp=temp.replace("*"," ")
            #critical point is below.
            for line in lines:
                if line==tempOftemp:
                    idx=lines.index(line)
                    lines[idx]=temp+"\n"
            a_file=open("books.txt","w")
            a_file.writelines(lines)
            a_file.close()
            print("\nYou checked out the book below succesfully!")
            print("\n--> "+temp)
    return temp
#9th
def checkoutBook2aStudent():
    user, theBook=userLogin(), checkoutBook()
    data=user+" "+theBook+"\n"
    f=open("borrowedBooks.txt","a")
    f.writelines(data)
    f.close()

openApp=input("Welcome to the library to open this app, please type 'open': ")
if openApp.upper()=="OPEN":
    print("App is opening...")
    time.sleep(0.65)
    print("\nThe app has been opened. You can see options below.")
    menu()
    mainMenuInput = int(input("\nWhat action would you like to do?: "))
    while mainMenuInput != 0:
        if mainMenuInput==1:
            f = open("./books.txt","r")
            books = f.readlines() 
            listAllBooks(books)
            f.close()
        elif mainMenuInput==2:
            time.sleep(0.5)
            print("Looking for checked books...")
            time.sleep(1.0)
            print("\nYou can see the checked out books below.\n")
            checkedBooks()
        elif mainMenuInput==3:
            addNewBook()
        elif mainMenuInput==4:
            findByISBN()
        elif mainMenuInput==5:
            searchBookbyName()
        elif mainMenuInput==6:
            checkoutBook2aStudent()
        menu()
        mainMenuInput = int(input("\nWhat action would you like to do?: "))
else:
    time.sleep(0.5)
    print("\nSorry, I cannot understand that. Please run again the code.")