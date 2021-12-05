
# name = input("my name is:")
# print("my name is : " + name)


# gender = input("my gender is :")
# print("my gender is :" + gender )


# age = input("my age is :")
# print("my age is ",age ) 


# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# operation= input("(+) to add / (-) to subtract / (*) to multiplication / (/) to division: ")


# def add(val1, val2):
#     print(int(val1) + int(val2))



# def subtract(new1, new2):
#     print(int(new1) - int(new2))


# def multiplication(p1, p2):
#     print(int(p1) * int(p2))

# def division(d1, d2):
#     print(int(d1) / int(d2))    


# if operation == "+":
#     add(num1, num2) 
# elif operation == "-":       
#     subtract(num1, num2)
# elif operation == "*":
#     multiplication(num1, num2)
# elif operation == "/":
#     division(num1, num2) 
 
    


# def myTeam(number):
 
#     print("my team member number is ",number)

# myTeam(20)



# def myTeam(firstnumber, name, marks):

#     print("priya T-shirt number is", firstnumber, "and her friend", name ,"achive", marks,"grade",)

# myTeam(7, "riya", 88)
# myTeam(10, "kishu",92)
# myTeam(12,"tulsi", 66)    


# def myTeam(*teamdetail):

#     print("priya T-shirt number is", teamdetail[0], "and her friend", teamdetail[1] ,"achive", teamdetail[2],"grade",)

# myTeam(7, "riya", 88)
# myTeam(10, "kishu",92)
# myTeam(12,"tulsi", 66)   


# def myTeam(firstnumber, name, marks):

#     print("priya T-shirt number is", firstnumber, "and her friend", name ,"achive", marks,"grade",)

# myTeam(firstnumber=7, name="riya", marks=88)
   

# def myTeam(**teamdetail): 
      
#     print("priya T-shirt number is", teamdetail["firstnumber"], "and her friend", teamdetail["name"] ,"achive", teamdetail["marks"],"grade",)

# myTeam(firstnumber=7, name="riya", marks=88)    




# def myteam(marks = 74):
#     print("my grads", marks )

# myteam(56)
# myteam(78)
# myteam()


# def classGrade(num):
#     newSum = num + 20
#     return newSum

# sum = classGrade(15) + 5
# print(sum)

# sum2 = classGrade(20) + 10
# print(sum2)

# sum3 = classGrade(25) + 15
# print(sum3)


# def classgrade(grade):
#     grade 
#     return grade

# marks = classgrade(10) + 15
# print(marks)  

# marks1 = classgrade(15) + 20
# print(marks1)  

# def classgrade(*grade):
#     for x in grade:
#         if x <= 22:
#             print("i am on my way", x)

# classgrade(22,25,78,10,8)            


# a=9
# b=8
# c=sum((a,b))
# print(c)

# def function1():
#     print("i am in function")

# function1()

# def function1(a,b):
#     print("i am in function", a*b)

# function1(10, 20)    

# def function(a,b):
#     average=(a+b)/2
#     print(average)

# function(10, 40)    


# def function(a,b):
#     average=(a+b)/2
#     print(average)

#     return average
# p= function(10, 40)
# print(p)


# def greet():
#     print("hii there")
#     print("welcome user")
#     print("learn python")

# greet()


# def greet(firstname , lastname):
#     print("hii there", firstname "and", lastname)
#     print("welcome user", lastname)
#     print("learn python", firstname)

# greet("priya", "sahil")

# def number(*numbers):
#     for x in numbers:
#         print(x)

# number(2,5,6,7,9)

# def number(*numbers):

#     ver=1
#     for x in numbers:
#         ver = ver * x
#     return ver

# print(number(2,5,6,7,9))


# def number(*unknow):
#     if unknow % 2 == 0  and unknow % 2 == 1:
#         print("fizzbuzz")
#     elif unknow % 2 == 1:
#         print("buzz")
#     elif unknow % 2 == 1 and unknow % 2 == 0:
#         print("fizz")


# number(for x in range(1,100,1))    


# def name(*names):
#     for x in names:
#         abc= x.upper()
#         print(abc)

# name("sahil", "priya",)    


# def tem_celsius(*abc):
#     tem_fehrenheit = []

# for x in abc:
#     ver=(x * 9/5) + 32
#     tem_fehrenheit.append(ver)

# print(tem_fehrenheit)
# tem_celsius(20,90,45,67,55,70,19)    


numbers=[1, 14, 7, 9, 20, 10, 17, 15, 11, 8]

def myfunction(myNums):

    squares=[]
   

    for x in numbers:
        if x % 2 == 1:
            sq = x * x        
            squares.append(sq)            
    return squares 
def cubesfunction(myNums):
    cubes=[]             
    for x in numbers:
        if x % 2 == 0:
            cu = x * x * x
            cubes.append(cu)
    return cubes       

print("squares num", myfunction(num))
print("cubes num", myfunction(num))


# num = [1,4,6,3,5,7,8,4,6,8,9]

# def evenFunction(myNums):
#     evenNumber = []

#     for myNUM in myNums:                                    

#         if myNUM % 2 == 0:                                 
#             evenNumber.append(myNUM)                              
#     return evenNumber                                         

# def oddFunction(myNums):                                          
#     oddNumber = []
                                                            
#     for myNUM in myNums:
#         if myNUM % 2 != 0:
#             oddNumber.append(myNUM)
#     return oddNumber
  

# print('Even number list', evenFunction(num))
# print('Odd number list', oddFunction(num))