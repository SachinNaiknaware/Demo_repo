# Python मध्ये OOP म्हणजे कोडला objects आणि classes मध्ये विभागून modular, reusable आणि logical बनवणे.

# Classes (क्लासेस)
# Class म्हणजे: Object तयार करण्यासाठीचा ब्लूप्रिंट.

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# Object म्हणजे: Class चा instance (प्रत्यक्ष वापर).
# p1=person("Sachin",24)
# print(p1.name)
# print(p1.age)


# Method Calls (मेथड कॉल्स)
# Class मध्ये functions म्हणजे methods.


# class person:
#     def greet(self):
#         print("Hello !...")
        
# p1=person()
# p1.greet() #metjos call

# Inheritance and Its Types (वारसा व त्याचे प्रकार)
# Inheritance म्हणजे: एका class चे गुणधर्म दुसऱ्या class मध्ये वापरणे
# Inheritance means one class used to another class


# Types:

# Single Inheritance

# Multiple Inheritance

# Multilevel Inheritance

# Hierarchical Inheritance

# Hybrid Inheritance


# class parent:
#     def show(self):
#         print("Parent Claas !........")
# class child(parent):
#     pass
# c=child()
# c.show() #parent class


# Summary Table
# Type	           Structure	                Example Relation
# Single	   One parent → One child	        Parent → Child
# Multiple	T  wo or more parents → One child	    Father + Mother → Child
# Multilevel	Grandparent → Parent → Child	Grandfather → Father → Son
# Hierarchical	One parent → Many children	    Parent → Child1, Child2
# Hybrid	      Combination of above	        School → Teacher, Student → Monitor

#####  1   single inhereurns
# class parent:
#     def show(self):
#         print("Parent class !......")
# class child(parent):
#     pass
# c=child()
# c.show()


# example of one parent class ans one child class
# class parent:
#     def display_parent(self):
#         print("This is the parents class ! ........")
# class child(parent):
#     def display_child(self):
#         print("This is the child class !............")
# c=child()
# c.display_child()
# c.display_parent()

##### multiple inheritance 
# A class inheritance from more one parent class
# class father:
#     def show_father(self):
#         print("Father is property !............") 
# class mother:
#     def show_mother(selt):
#         print("Mother properie !..........")
# class child(father,mother):
#     def show_child(self):
#         print("Child property")
# obj=child()
# obj.show_father() 
# obj.show_mother()
# obj.show_child()

# class engine: # parent class 1
#     def start(self):
#         print("Engine is started ")
# class musicsystem: #parent class 2
#     def play_music(self):
#         print("Playing music !..............")
# class car(engine,musicsystem): # child class inherits form the both class
#     def drive(self):
#         print("Car is Driving !.............")
        
# obj=car()
# obj.start()
# obj.play_music()
# obj.drive()


### 3 Multilevel Inheritanc A class inherits from another class, which itself is inherited from another 
# class(Grandparent → Parent → Child)
# class Grandfather:
#     def show_grandfather(self):
#         print("Grand-Father-Legacy")
# class Father(Grandfather):
#     def show_father(self):
#         print("Father Assets")
# class Son(Father):
#     def show_son(self):
#         print("Son achivement")
# obj=Son()
# obj.show_grandfather()
# obj.show_father()
# obj.show_son()


# class Grandfather:
#     def property(self):
#         print("Grandfather has: farmland")
# class Father(Grandfather):
#     def house(self):
#         print("Fathe:- Built a new house")
# class Son(Father):
#     def car(self):
#         print("Son have Xuv car")
# obj=Son()
# obj.property()
# obj.house()
# obj.car()


#### 4. Hierarchical Inheritance One parent class → Multiple child classes
#In Hierarchical Multiple child class inherit from the same parent class
# class parent:
#     def head_parent(selt):
#         print("Parent Class")
# class child1(parent):
#     def head_child_1(self):
#         print("Child one class")
# class child2(parent):
#     def head_child_2(slef):
#         print("Child second class")
# obj1=child1()
# obj2=child2()
# obj1.head_parent()
# obj1.head_child_1()
# obj2.head_parent()
# obj2.head_child_2()

#class parent:
#     def home(self):
#         print("Parents own familly house")
# class son(parent):
#     def bike(self):
#         print("Son has sport bike ")
# class dauthter(parent):
#     def car(self):
#         print("Daughter have own car")
        
# s = son()
# d = dauthter()

# s.home()
# s.bike()

# d.home()
# d.car()


####5.  Hybrid Inheritance
# Combination of two or more types of inheritance (For example: multiple + multilevel)
#Hybrid Inheritance is a combinattion off two or more types of inheritances in single program
# it allow classes to  reuse code from diffrent sources while keeping relationship organized

# class School:
#     def show_school(self):
#         print("This is the school")
# class Teacher(School):
#     def show_teacher(self):
#         print("This is teacher")
# class Student(School):
#     def show_student(self):
#         print("This is Student")
# class Monitor(Teacher,Student):
#     def show_moniter(self):
#         print("This is the moniter")
# obj=Monitor()
# obj.show_school()
# obj.show_teacher()
# obj.show_student()
# obj.show_moniter()

# Base class
# class Vehicle:
#     def start(self):
#         print("Vehicle started")

# # Single inheritance branch
# class Engine(Vehicle):
#     def engine_info(self):
#         print("Engine is ready")

# # Another branch
# class Battery:
#     def battery_info(self):
#         print("Battery charged")

# # Hybrid: inherits from both Engine (which already inherits Vehicle) and Battery
# class ElectricCar(Engine, Battery):
#     def feature(self):
#         print("Electric car running smoothly")

# Object
# tesla = ElectricCar()
# tesla.start()         # From Vehicle
# tesla.engine_info()   # From Engine
# tesla.battery_info()  # From Battery
# tesla.feature()       # From ElectricCar


# Overloading (ओव्हरलोडिंग)
# Python मध्ये method overloading थेट नाही, पण default arguments वापरून करता येते.

# class math:
#     def add(slef, a=0,b=0,c=0):
#         return a+b+c
# m=math()
# print(m.add(2,3))
# print(m.add(2,3,4))


# Overriding (ओव्हररायडिंग)
# Child class मध्ये parent ची method redefine करणे.
#class Parent:
#     def show(self):
#         print("Parent method")

# class Child(Parent):
#     def show(self):
#         print("Child method")

# c = Child()
# c.show()  # Child method

# Data Hiding (डेटा लपवणे)
# Private variables वापरून data सुरक्षित ठेवणे.

# class Bank:
#     def __init__(self):
#         self.__balance = 1000  # private

#     def show_balance(self):
#         print(self.__balance)

# b = Bank()
# b.show_balance()  # 1000


# Operator Overloading (ऑपरेटर ओव्हरलोडिंग)
# Operators (+, -, *) objects साठी redefine करणे.
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

# p1 = Point(2, 3)
# p2 = Point(4, 5)
# p3 = p1 + p2
# print(p3.x, p3.y)  # 6 8
