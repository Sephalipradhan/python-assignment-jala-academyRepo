#Creat an abstract class with abstract and non abstract method
from abc import ABC, abstractmethod
 
class Polygon(ABC): #base class / super class
 
    @abstractmethod
    def noofsides(self):
        pass
 
class Triangle(Polygon): #subclass
 
    # overriding abstract method
    def noofsides(self):
        print("Triangle: I have 3 sides")
 
class Pentagon(Polygon): #subclass
 
    # overriding abstract method
    def noofsides(self):
        print("Pentagon: I have 5 sides")
 
class Hexagon(Polygon): #subclass
 
    # overriding abstract method
    def noofsides(self):
        print("Hexagon: I have 6 sides")
 
class Quadrilateral(Polygon): #subclass
 
    # overriding abstract method
    def noofsides(self):
        print("Quadrilateral: I have 4 sides")
 
# Driver code
# Creating the objects to call the abstract method.
R = Triangle()
R.noofsides()
 
K = Quadrilateral()
K.noofsides()
 
R = Pentagon()
R.noofsides()
 
K = Hexagon()
K.noofsides()
