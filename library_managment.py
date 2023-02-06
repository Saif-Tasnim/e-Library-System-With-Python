class User:
    user_list = []
    def __init__(self,name,roll,password) -> None:
        self.name= name
        self.roll = roll
        self.password = password
        self.borrow_book = []
        self.return_book = []
        self.user_list.append(self)

class Library:
    def __init__(self,book_list) -> None:
        self.book_list = book_list
    
    def borrow_book(self,bookName,user):
        for book in self.book_list:
            # print("Book name : ",book)
            if book == bookName:
               if book in user.borrow_book:
                 print("\t______________________________________")
                 print(f"\tReturn Your {book} Book First")
                 return
               if  self.book_list[book] == 0:
                  print(f'{bookName} is not available at this moment')
                  return
               
               self.book_list[book] -= 1
               user.borrow_book.append(bookName)
               print("\t______________________________________") 
               print("\tHere it is your book. Please return it on time ")
               return
        print("\t______________________________________") 
        print(f'\t{bookName} is not available')
        return    


    def returned_book(self,bookName,user):
        for book in user.borrow_book:
            if book == bookName:
                self.book_list[book] += 1;
                user.borrow_book.remove(book)
                user.return_book.append(book)
                print("\t______________________________________")
                print("\tYour Book Received By Us. Thanks For Your Return")
                return
        print("\t______________________________________")
        print(f"\tYou Have not Borrow {bookName} this book. What do you want to return ?")



library = Library({'English' : 2, 'Bangla' : 7 , 'Math' : 12, 'Islamic':23 , 'ICS' : 0 })

currentUser = None
print("\t\t______________________________________")
print("\n\t\tWelcome To e-Library Management System !")
print("\t\t______________________________________")

while True:
    if currentUser == None:
       
        print("\n\nLog In Or Create Account : \n")
        print("1. For Log In")
        print("2. For Create New Account")
        option = input('\nEnter your choice : ')
        if(option == '1'):
            roll = int(input("Enter Roll No :"))
            password = input("Enter Your Password : ")
            find_match = False;
            for user in User.user_list:
                if user.roll == roll and user.password == password:
                    currentUser = user
                    find_match = True
                    print("\t____________________________________") 
                    print("\t\tSuccessfully Logged In")
            
            if find_match == False:
                print("\t\t____________________________________")
                print("\t\tNo Data Found. Create An Account First")
        
        else :
            name = input("Enter Your Name : ")
            roll = int(input("Enter Your Roll : "))
            password = input("Set Your password : ")
            find = False;
            for old in User.user_list:
                if old.name == name and old.roll == roll :
                    print("\t____________________________________") 
                    print("\t\tUser Already Exist. Please Log In ")
                    find = True 
                
            if find == False:
                user = User(name,roll,password)
                print("\t____________________________________")
                print("\t\tSuccessfully Created Account ")
    
    else:
        print("\n\n________________________")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. My Profile")
        print("4. Account Setting")
        print("0. Log Out")
        
        option = input('Select Your Option : ')
        
        if option == '1':
            name = input("Enter The Book name : ")
            library.borrow_book(name,currentUser)
            
        
        elif option == '2':
             name = input("Enter The Book name : ")
             library.returned_book(name,currentUser)
        

        elif option == '3' :
            print("\t____________________________________")
            print("\t\t\tUser Details") 
            print("\t____________________________________")
            print("User Name : ",currentUser.name)
            print("User Roll No : ",currentUser.roll)
            print("Borrow Book List : ",currentUser.borrow_book)
            print("Return Book List : ",currentUser.return_book)
        

        elif option == '0':
            currentUser = None