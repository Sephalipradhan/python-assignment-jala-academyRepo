class A():  
    def display(dp):
        print("Display Inside class A ")
 # class A show method    
    def show(self):
        print("Show Inside class A")
    
# Inherited or Sub class (Note A in bracket) 
class B (A): 
    def print(pt):
        print("Print Inside class B")    
    # class B show method
    def show(self):
        print("Show Inside class B")
    
# Inherited or Sub class (Note B in bracket) 
class C (B): 
          
    # class C show method
    def show(self):
        print("Show Inside class C ")         
    
# Driver code 
s = A()
s.display()
k= B()
k.print()
g = C()   
g.show()