from unicodedata import name


class A:
    # default constructor
    def __init__(self):
     self.name = "Kashish"
     # a method for printing data members
    def print_A(self):
        print(self.name)
# creating object of the class
obj = A()
# calling the instance method using the object obj
obj.print_A()

class B(A):
    def __init__(self):
     self.name = "KG"
    def print_B(self):
        print(self.name)
obj1 = B()
obj1.print_B()

class C:
    # public data member
    name = None

     # protected data members
    _roll = None 

     # private data member
    __branch = None

    # constructor
    def __init__(self,name,roll,branch):
        self.name = name  
        self._roll = roll
        self.__branch = branch  
    def dsiplayName(self):
        print("Name:",self.name)
        # protected member function
    def _displayRoll(self):
         # accessing protected data members
        print("Roll:",self._roll)

         # private member function 
    def __displayBranch(self):
        # accessing private data members
        print("Branch:",self.__branch)

         # public member function
    def access__displayBranch(self):     
          # accessing private member function
        self.__displayBranch()

class D(C):
    def __init__(self,name, roll, branch):
        super().__init__(name,roll, branch)
      # public member function
    def access_displayRoll(self):            
         # accessing protected member functions of super class
        self._displayRoll()

# creating objects of the derived class    
obj = D("Kashish", 5 , "CSE")
# calling public member functions of the class  
obj.dsiplayName()
obj.access_displayRoll()
obj.access__displayBranch()      