


# class MyAge:
#     v1 = 25
#     v2 = 45

# obj = MyAge()

# accessVar = obj.v2
# print(accessVar)
# print(obj)


# class BirthYear:
#     priya = 1998
#     jaanvi = 2000
#     sahil = 1995
#     riya = 2003
#     charmi = 1992

# obj = BirthYear()

# accessyear = obj.riya   # first way to print value with using veriable
# accessyear1 = obj.sahil
# print(accessyear1)
# print(accessyear) 

# print(obj.riya) # second way to print value # i can print value directly without using veriable 


# class employer:
#     def __init__(self,name, year, age, city ):
#         self.name = name
#         self.year = year
#         self.age = age
#         self.city = city

# obj = employer("priya", 1998, 23, "surat")

# accessdetail = obj.name
# print("my name is ", accessdetail)
# accessdetail1 = obj.age
# print("i am ",accessdetail1, "years old" )

# ------------------------------------------


# class Employer:
#     def __init__(self,name, year, age, city ):
#         self.name = name
#         self.year = year
#         self.age = age
#         self.city = city

#     def MyInfo(self):
#         print("hii my name is ", self.name)
#         print("i was born in", self.year)
#         print("i am ", self.age , "years old")
#         print("i am live in", self.city) 


# obj = Employer("priya", 1998, 23, "surat")
# obj.MyInfo()

# -----------------------------------------

        



# class Player:
#     def __init__(Data, name, game, city):
#         Data.name = name
#         Data.game = game
#         Data.city = city

#     def Detail(abc):
#         print("my name is", abc.name)  

#     def otherdetail(xyz):
#         print("i am playing", xyz.game)

#     def location(pqr):
#         print("i am live in", pqr.city)

# gamedata = Player("priya", "cricket", "surat")
# gamedata.Detail()
# gamedata.otherdetail()
# gamedata.location()


# class Player:
#     def __init__(Data, name, game, city):
#         Data.name = name
#         Data.game = game
#         Data.city = city

#     def Detail(abc):
#         print("my name is", abc.name, "i am playing", abc.game, "and i am live in ", abc.city)  


# gamedata = Player("priya", "cricket", "surat")
# gamedata.Detail()


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)


class Player:
    def __init__(Data, name, game, city):
        Data.name = name
        Data.game = game
        Data.city = city

    def Detail(abc):
        print("my name is", abc.name, "i am playing", abc.game, "and i am live in ", abc.city)  

gamedata = Player("priya", "cricket", "surat")
gamedata.city = "ahemdabad"
gamedata.Detail()