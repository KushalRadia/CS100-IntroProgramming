# OOPS - OBJECT ORIENTED PROGRAMMING IS A PROGRAMMING PARADIGM WHERE THE SOFTWARE DESIGN REVOLVES AROUND DATA OR OBJECTS RATHER THAN FUNCTIONS.
# IN PROCEDURE ORIENTED PROGRAMMING , PROGRAMS HAS FUNCTIONS.
# IN OBJECT ORIENTED PROGRAMMING , PROGRAM'S MAIN FOCUS IS ON OBJECTS OR DATA.
# ADAVNTAGES OF USING OOPS - HELPS TO MIMIC REAL WORLD ENTITIES AND THEIR INTERACTIONS , HELPS IN CODE REUSABILITY , HELPS IN ORGANISATION AND MAINTAINABILITY OF CODE.

# CLASSES ----
# THEY ARE USER DEFINED DATA TYPES.
# THEY ARE BLUEPRINT / TEMPLATE FOR AN OBJECT.

# OBJECT ----
# AN OBJECT IS AN INSTANCE(VARIABLE) OF TYPE CLASS.
# IT MIMICS REAL WORLDS ENTITIES.

# ALL THE INSTANCES/OBJECTS HAVE THE ATTRIBUTES AND METHODS(FUNCTIONS) OF THE CLASS.

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# self IS A BY-DEFAULT PARAMETER WHICH PASSES BY ITSELF. THE OBJECT FOR WHICH THE FUNCTION IS CALLED , THAT OBJECT IS PASSED AS self . NOW FOR ACCESSING ANY ATTRIBUTES OR FUNCTIONS OF ANY CLASS , WE CAN USE "." FOR THAT.
class student:
    def set_name(self , name):
        self.name = name
    def get_name(self):
        return self.name
student1 = student()
student1.set_name("aahana")
print(student1.name)        
student2 = student()
student2.set_name("purvi")
print(student2.get_name())

class rectangle:
    def set_dimensions(self , width , height):
        self.width = width
        self.height = height
    def area(self):
        self.area = self.height*self.width
        return self.area
    def perimeter(self):
        return 2*(self.width + self.height)
rectangle1 = rectangle()
height = float(input("Enter the height of the rectangle : "))
width = float(input("Enter the width of the rectangle : "))
rectangle1.set_dimensions(width , height)
print("The height of rectangle is : " , rectangle1.height)
print("The width of rectangle is : " , rectangle1.width)
print("The area of the rectangle is : ", rectangle1.area())
print("The perimeter of the rectangle is : ", rectangle1.perimeter())

# CLASS CONSTRUCTOR IS A SPECIAL FUNCTION THAT GETS INVOKED EVERYTIME AN OBJECT IS CREATED FOR THAT CLASS. 
# SYNTAX OF CLASS CONSTRUCTOR ---
# class calss_name:
#   def __init__(self , parameter1 , parameter2 , ...):
# HERE WE USE TWO UNDERSCORES WITH init KEYWORD.
class rectangle:
    def __init__ (self , height1 , width1):
        print(f"The height of rectangle is : {height1} and the width of the rectangle is : {width1}")
        self.height = height1
        self.width = width1
    def area(self):
        self.area = self.height*self.width
        return self.area
    def perimeter(self):
        return 2*(self.width + self.height)
height1 = float(input("Enter the height of the rectangle : "))
width1 = float(input("Enter the width of the rectangle : "))
rectangle1 = rectangle(height1 , width1)
print("The area of the rectangle is : ", rectangle1.area())
print("The perimeter of the rectangle is : ", rectangle1.perimeter())
rectangle2 = rectangle(7,8)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# ATTRIBUTES.....................................................................
# ATTRIBUTES ARE OF TWO TYPES -----
# 1) CLASS ATTRIBUTES - is defined inside the class and all object instances will have these attributes. 
# 2) INSTANCE ATTRIBUTES - are specific to a particular instance/object.
class industry:
    def worker(self,name):
        self.name = name     # CLASS ATTRIBUTE
        return name    
name1 = input("Enter your name : ")       
name2 = input("Enter your name : ")
worker1 = industry()
worker2 = industry()
print(worker1.worker(name1))
print(worker2.worker(name2))
worker1.post = "registrar"    # INSTANCE ATTRIBUTE
print(f"Post of {name1} is {worker1.post}")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# ACCESS MODIFIERS - THEY CONTROL THE VISIBILITY/ACCESS OF CLASS ATTRIBUTES AND FUNCTIONS.
# 1) PUBLIC MODIFIER - FUNCTIONS AND ATTRIBUTES ARE ACCESSIBLE OUTSIDE THE CLASS. BY DEFAULT ALL THE ATTRIBUTES AND FUNCTIONS ARE PUBLIC MODIFIERS.
class ABC():
    def __init__(self):
        self.public_modifier_attribute = 10   # PUBLIC ATTRIBUTE
        self.public_access_modifier = None
    def public_function(self):    # PUBLIC FUNCTION
        pass    
obj1 = ABC()
print(obj1.public_modifier_attribute)
obj1.piblic_access_modifier
obj1.public_function()

# 2) PROTECTED MODIFIER - FUNCTIONS AND ATTRIBUTES ARE ACCESSIBLE OUTSIDE THE CLASS BUT IT SHOULD NOT BE ACCESSED.IT IS ONLY ACCESSIBLE FROM INSIDE THE CLASS OR THE SUB-CLASS.  
class DEF():
    def __init__(self):
        self._protected_modifier_attribute = 10   # PROTECTED ATTRIBUTE
        self._protected_access_modifier = None
    def _protected_function(self):    # PROTECTED FUNCTION
        pass    
obj1 = DEF()
print(obj1._protected_modifier_attribute)
obj1._protected_access_modifier
obj1._protected_function()

# 3) PRIVATE MODIFIER - FUNCTIONS AND ATTRIBUTES ARE NOT ACCESSIBLE OUTSIDE THE CLASS.
class XYZ():
    def __init__(self):
        self.__private_modifier_attribute = 10    # PRIVATE ATTRIBUTE
    def __private_function(self):    # PRIVATE FUNCTION
        pass    
obj1 = XYZ()
print(obj1.__private_modifier_attribute) # THROWS ERROR AS WE ARE TRYING TO ACCESS ATTRIBUTE FROM OUTSIDE THE CLASS.
print(obj1.__private_function()) # THROWS ERROR AS WE ARE TRYING TO ACCESS ATTRIBUTE FROM OUTSIDE THE CLASS.

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# PROPERTIES OF OOPS.................................................................
# 1) INHERITANCE - IT IS THE PROPERTY OF OOPWHERE ONE CLASS CAN INHERIT PROPERTY(ATTRIBUTES AND FUNCTIONS) FROM ANOTHER CLASS. PARENT CLASS IS ALSO KNOWN AS SUPERCLASS AND CHILD CLASS IS ALSO KNOWN AS SUBCLASS.
class parent():
    def __init__(self):
        print("This is a parent class")
        self.attribute = True + False + True
class child(parent):     
    def __init__(self):
        super().__init__()      # super() is a keyword used to connect parent class with child class. CALLING CONSTRUCTOR OF SUPER CLASS.
        print("This is a child class")  
        print(self.attribute)  
child1 = child()
# TYPES OF INHERITANCE -----
# 1) SINGLE INHERITANCE - ONE PARENT CLASS AND ONE CHILD CLASS 
# 2) MULTIPLE INHERITANCE - MORE THAN ONE PARENT CLASS OF A SUBCLASS , LIKE class c(a,b): WHERE CLASS a , b ARE SUPERCLASSES OF CLASS c. 
# 3) MULTILEVEL INHERITANCE - CONTAINS BASE CLASS(GRANDPARENT CLASS) , INTERMEDIARY CLASS(PARENT CLASS) , DERIVED CLASS(CHILD CLASS) AND SO ON . 
'''
LIKE 
class a():
class b(a):
class c(b):
and so on ... 
THIS CLASS c HAS ALL THE ATTRIBUTES AND METHODS OF CLASS a .
'''
# 4) HIERARCHICAL INHERITANCE - HAS ONE BASE CLASS AND MULTIPLE CHILD CLASSES.
'''
LIKE
class a():
class b(a):
class c(a):
'''
# 5) HYBRID INHERITANCE - IS IS A MIX OF MULTILEVEL INHERITANCE AND HIERARCHICAL INHERITANCE.
'''LIKE
class a():
class b():
class c(a,b):
class d(c):
THIS CLASS d HAS ALL THE ATTRIBUTES AND METHODS OF class a , b , c .
'''

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# QUESTION : CREATE A BUS CHILD CLASS THAT INHERITS FROM THE VEHICLE CLASS. THE DEFAULT AFRE CHARGE OF ANY VEHICLE IS SEATING CAPACITY * 100 . IF VEHCILE IS BUS INSTANCE , WE NEED TO ADD AN EXTRA 10 % ON FULL FARE AS A MAINTAINENCE CHARGE . SO TOTAL FARE FOR BUS INSTANCE WILL BECOME THE FINAL AMOUNT = TOTAL FARE + 10% OF THE TOTAL FARE .
# EXAMPLE : VEHICLE FARE : 5000 , BUS FARE : 5500 .0 
class vehicle():
    def __init__(self , seating_capacity):
        self. seating_capacity = seating_capacity
    def get_fare(self):                                   # FUNCTION 1 
        return self.seating_capacity*100
class bus(vehicle):
    def __init__(self , seating_capacity):
        super().__init__(seating_capacity)
    def get_fare(self):                                   # FUNCTION 2
        vehicle_fare = super().get_fare()
        maintainence_fare = 0.1*vehicle_fare
        total_fare = vehicle_fare + maintainence_fare
        return total_fare
seating_capacity_bus= float(input("Enter seating capacity of bus : "))
seating_capacity_vehicle = float(input("Enter seating capacity of vehicle : "))
bus1 = bus(seating_capacity_bus)
vehicle1 = vehicle(seating_capacity_vehicle)
print("Total fare of bus is :" , bus1.get_fare())
print("Total fare of vehicle is :" , vehicle1.get_fare())
# IF I HAVE'NT CALL FUNCTION 2 THEN ONLY FUNCTION 1 WILL EXECUTE AS BUS IS A CHILD CLASS OF VEHICLE AND SAME FARE WILL BE DISPLAYED FOR BOTH CLASSES. IF SAME NAME FUNCTIONS ARE PRESENT IN CHILD CLASS AND PARENT CLASS THEN CHILD CLASS FUNCTION WILL INVOKE . IF CHILD CLASS FUNCTION IS ABSENT THEN PARENT CLASS FUNCTION WILL INVOKE .

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 2) POLYMORPHISM - IT ALLOWS OBJECTS OF DIFFERENT CLASSES TO BEHAVE AS OBJECTS OF THE SAME SUPERCLASS. 
class animal:
    def speaks(self):  # ABSTARCT METHOD WILL WHICH BE OVER-WRITTEN
        pass
class dog:
    def speaks(self):
        print("Barks")
class cat:
    def speaks(self):
        print("Meow")
class cow:
    def speaks(self):
        print("Mooo")               
dog1 = dog()
cat1 = cat()
cow1 = cow()
print(dog1.speaks())        
print(cat1.speaks())  
print(cow1.speaks())  
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
class animal:
    def speaks(self):  # ABSTARCT METHOD WILL WHICH BE OVER-WRITTEN
        pass
class dog:
    def speaks(self):
        return "Barks"
class cat:
    def speaks(self):
        return "Meow"
class cow:
    def speaks(self):
        return "Mooo"              
dog1 = dog()
cat1 = cat()
cow1 = cow()
print(dog1.speaks())        
print(cat1.speaks())  
print(cow1.speaks())  
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
class animal:
    def speaks(self):  # ABSTARCT METHOD WILL WHICH BE OVER-WRITTEN
        pass
class dog(animal):
    def speaks(self):
        print("Barks")
class cat(animal):
    def speaks(self):
        print("Meow")
class cow(animal):
    def speaks(self):
        print("Mooo")               
dog1 = dog()
cat1 = cat()
cow1 = cow()
dog1.speaks()        
cat1.speaks()
cow1.speaks() 
# POLYMORPHISM IS OF TWO TYPES: 
# 1) COMPILE-TIME POLYMORPHISM - THIS IS RESOLVED DURING COMPILE TIME MEANS IT IS DECIDED IN THE COMPILE TIME THAT WHICH INSTANCE WOULD BE INVOKE. THIS IS ACHEIVED THROUGH TWO METHODS - METHOD OVERLOADING AND OPERATOR OVERLOADING.
# METHOD OVERLOADING - IT ALLOWS US TO HAVE MULTIPLE METHODS WITH SAME NAME BUT DIFFERENT PARAMETERS.
# OPERATOR OVERLOADING IS ILLUSTRATED THROUGH THIS EXAMPLE:
class complex_number:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def __add__(self , other):
        return complex_number(self.real + other.real , self.img +  other.img)
complex1 = complex_number(3,4)
complex2 = complex_number(3,5)
complex3 = complex1 + complex2       
print(complex3.real , "+i" ,  complex3.img)
# 2) RUN-TIME POLYMORPHISM - THIS IS RESOLVED DURING RUN TIME. THIS SI ACHEIVED THROUGH METHOD OVERRIDDING.
class animal:
    def speaks(self):  # ABSTARCT METHOD WILL WHICH BE OVER-WRITTEN
        print("generic noise")
class dog(animal):
    def speaks(self):
        print("Barks")
class cat(animal):
    def speaks(self):
        print("Meow")
class cow(animal):
    def speaks(self):
        print("Mooo")               
dog1 = dog()
cat1 = cat()
cow1 = cow()
dog1.speaks()        
cat1.speaks()
cow1.speaks() 

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 3) ABSTRACTION - THIS ALLOWS TO FOCUS ON THE "WHAT " OF AN OBJECT RATHER THAN "HOW" OF AN OBJECT.AN ABSTRACT CLSS MAY CONTAIN ABSTRACT METHODS , WHICH MUST BE IMPLEMENTED BY ITS CONCRETE SUBCLASSES.

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 4) ENCAPSULATION - IT BUNDLES THE ATTRIBUTES AND THE METHOD TOGETHER IN ONE ENTITY KNOWN AS CLASS. BECAUSE OF THIS A PROTECTION BARRIER OF A DTA FROM UPDATION IS CREATED AND SECONDLY , IT HIDES AWAY UNNECCESARY DETAILS.

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# EXCEPTION HANDLING IN OOPS - 
# IN TRY BLOCK , WE WRITE CODE WHICH MIGHT THROW ERROR(EXCEPTION)
# IF ERROR OR EXCEPTION THROWS THEN THIS EXCEPT BLOCK WILL RUN. WE CAN ALSO MENTION EXCEPTION TYPE LIKE VALUE-ERROR , TYPE-ERROR, ZERO DIVISON ERROR , EXCEPTION(includes all errors.)
# IN FINAALY BLOCK , WE WRITE THE CODE WHICH WILL BE EXECUTED REGARDLESS OF EXCEPTION.

# QUESTION: IMPLEMENT EXCEPTION HANDLING IN PYTHON BY SHOWING DIVISION OPERATION.YOU CAN SHOW EXCEPTION - "ZeroDivsionError".
# INPUT : a = 10 , b = 2 
# OUTPUT : CLEANUP : DIVISION OPERATION COMPLETED.
# INPUT : a = 5 , b = 0
# OUTPUT : ERROR : CANNOT DIVIDE BY ZERO.
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
try:  
    print("Cleanup : Divsion operation completed.")
    result =  num1 / num2 
except ZeroDivisionError:
    result = None
    print("Cannot divide by zero.")
finally:
    print("Result is : " , result)


