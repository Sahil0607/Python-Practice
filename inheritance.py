

# class Game:
#     def __init__(Data, name, game, city):
#         Data.name = name
#         Data.game = game
#         Data.city = city

#     def Detail(abc):
#         print("my name is", abc.name, "i am playing", abc.game, "and i am live in ", abc.city)  

# gamedata = Game("priya", "cricket", "surat")
# # gamedata.city = "ahemdabad"
# gamedata.Detail()


# class players(Game):
#     pass

# x = players("kirtan", "football","baroda")
# x.Detail()


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()

# class collage:
#     def __init__(self, students, teachers, stremChoice ):
#         self.students = students
#         self.teachers = teachers
#         self.stremChoice = stremChoice

#     def accessproperty(self):
#         print("all ",self.students,"my", self.teachers,"and", self.stremChoice)
       

# class school(collage):
#     pass

#     def __init__(self, students, teachers , stremChoice, classes, board):
#         self.students = students
#         self.teachers = teachers
#         self.stremChoice = stremChoice
#         self.classes = classes
#         self.board =  board

#     def accessproperty(self):
#         print("all",self.classes, "all", self.board )
        
            

# x = school(400, 15, 10, 20, 67 )
# x.accessproperty()        

# --------------------------------------------------------


# class family:

#     def __init__(self, grandFather, father, brother):
#         self.gFather = grandFather
#         self.father = father
#         self.brother = brother    

#     def accessname(self):
#         print(self.gFather)
#         print(self.father)
#         print(self.brother)

# class children (family):
#     pass

# x = children("nits", "mike", "olsen")
# x.accessname()


# --------------------------------------------------------------

# class birds:
#     def __init__(self, name, legs, wings, eyes ):
#         self.name = name
#         self.legs = legs
#         self.wings = wings
#         self.eyes = eyes

#     def accessdetails(self):
#         print(self.name, self.legs, self.wings, self.eyes)


# class picock(birds):

#     def __init__(self, name, legs, wings, eyes):
#         birds.__init__(self, name, legs, wings, eyes)

# x = picock("picock", 2, True, 2)   
# x.accessdetails()     
       
# # --------------------------------------------------------

# class teacher:
#     def __init__(self, job, standard):
#         self.job = job
#         self.standard = standard

#     def accessdetail(self):
#         print(self.job, self.standard)

# class students(teacher):
#     def __init__(self, job, standard):
#         teacher.__init__(self, job, standard)
#         self.higherStudy = False
#         self.subject = "subject"

# x = students("professional", "1 to 5")
# x.accessdetail()

# print(x.higherStudy)  
# print(x.subject)      
   
# # --------------------------------------------------------


# class grandFamily:
#     def __ini__(self, gfname, gmname ):
#         self.gfname = gfname 
#         self.gfname = gmname

#     def accessname(self):
#         if self.gfname == "john":
#             print("yes he is my grand father and his name is",self.gfname)

#         elif self.gfname == "mariya":
#             print("her name is", self.gfname)

   
# class presentFamily(grandFamily):
#     def __init__(self, gfname, gmname):
#         teacher.__init__(self, gfname, gmname)
#         self.child = 2
       

# x = presentFamily("john", "mariya")
# x.accessname()
# # y = presentFamily("john1", "mariya2")
# # print(y.presentFamily)
# print(x.child)  
   
# --------------------------------------------------------

# class A:
#     def feature1(self):
#         print("feature 1 working")

#     def feature2(self):
#         print("feature 2 working")

# class B(A):
#     def feature3(self):
#         print("feature 3 working")

#     def feature4(self):
#         print("feature 4 working")

# class C(B):
#     def feature5(self):
#         print("feature 5 working")
                


# A1 = A()

# A1.feature1()
# A1.feature2()

# b1 = B()

# b1.feature1()

# b1.feature3()


# c1 = C()
# c1.feature4()
# c1.feature1()

# --------------------------------------------  
#  
# class A:
#     def feature1(self):
#         print("feature 1 working")

#     def feature2(self):
#         print("feature 2 working")

# class B:
#     def feature3(self):
#         print("feature 3 working")

#     def feature4(self):
#         print("feature 4 working")

# class C(A,B):
#     def feature5(self):
#         print("feature 5 working")

# C1 = C()
# C1.feature1()
# C1.feature2()
# C1.feature3()       
# C1.feature4()
# C1.feature5()

# B1 = B()
# # B1.feature1()
# B1.feature3()


# --------------------------------------------

# class Animal:
#     def speck(self):
#         print("animal speaking")

# class Dog(Animal):
#     def bark(self):
#         print("dog barking")

# x = Dog()
# x.bark()
# x.speck()                

# -------------------------------------------------


# class Animal:
#     def speck(self):
#         print("animal speaking")

# class Dog:
#     def bark(self):
#         print("dog barking")

# class puppy(Animal,Dog):
#     def barking(self):
#         print("puppy is barking")

# # x = Dog()
# # x.bark()
# # x.speck()

# y = puppy()
# y.bark()
# y.speck()
# y.barking()

# -------------------------------------------------




# class calculation1:
#     def sum(self,a,b):
#         return a + b
 
# class calculation2:
#     def multiplication(self,c,d):
#        return c * d

# class divide1(calculation1, calculation2):
#     def divide(self,e,b):
#         return e/b

# d = divide1()
# print(d.sum(100,50))
# print(d.multiplication(10,40))
# print(d.divide(20,70))        


# class Vehical: 
#     def __init__(self,name,mileage, capacity):
#         self.n = name
#         self.mile = mileage
#         self.cap = capacity

#     def printinfo(self):
#         print("i have a", self., "that gives mileage of", self.mile, "and has capacity of" , self.cap, "people !!" )

# class MyCar(Vehical):
#     pass

# x = MyCar("honda city", 10, 20 )
# x.printinfo()

      
     
y = 10

def test():
    print("my num", y)
    global y
    y = "priya"
    # print("..", y)

test()
print(y)