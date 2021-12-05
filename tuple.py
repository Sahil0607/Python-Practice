
# def numbers():
#     newtuple=()
#     xyz=list(newtuple)
#     for x in range(1,50,1):
#         if x % 2 == 0:
#             xyz.append(x)
#     newtuple=tuple(xyz) 
#     return newtuple          

# print(numbers())          
       

# ----------------------------------------------

# def checkOddEvenNum():
#     evenList = ()
#     oddList = ()
#     xyz=list(evenList)
#     abc=list(oddList)
#     for val in range(1, 20, 1):
#         if val % 2 == 0:
#             xyz.append(val)
#             evenList=tuple(xyz)
#         else:
#             abc.append(val)
#             oddList=tuple(abc)

#     total = [evenList,oddList]
#     return total        
            
        
# print("even number",checkOddEvenNum()[0])
# print("odd number",checkOddEvenNum()[1])

# ----------------------------------------------
# namesOfmember=("priya", "jaanvi", "shreya", "riya")
# def names(name):
#     capitalName=[]
#     for x in name:
#         abc=x[0:2].upper()+ x [2:]
#         capitalName.append(abc)
#         convert=tuple(capitalName)
#     return convert

# print(names(namesOfmember))

# ----------------------------------------------

# namesOfMember=("pen", "pencile", "book")
# def names(name):
#     capitalLastName=[]

#     for x in name:
#         abc = x[0:-1]+ x[-1].upper()
#         capitalLastName.append(abc)
#         convert=tuple(capitalLastName)
#     return convert

# print(names(namesOfMember))

# ----------------------------------------------

# namesOfMember=("pen", "pencile", "book", "wardrobe","chair", "table","laptop")
# def names(name):
#     removename=[]
#     for idx, remove in enumerate(name):
#         if idx != 0 and idx !=2 and idx !=4:
#             removename.append(remove)
#             leftname =tuple(removename)
#     return leftname
            
# print(names(namesOfMember))


# ----------------------------------------------

# numbers = (20,10,2,6,63,97,34,23,13,11,3)
# def num(number):
#     newtuple=()
#     xyz=list(newtuple)
#     total=0
#     for x in number:
#         total= total + x

#     xyz.append(total)
#     newtuple= tuple(xyz)
#     return newtuple
   
# print(num(numbers))

# ----------------------------------------------

# monthName=("jan", "feb", "march", "april", "may")
# def names(name):
    
#     newlist=[]
#     ver="abc2021"

#     for x in name:
#         abc= ver + x
#         newlist.append(abc)
#     change= tuple(newlist)
#     return change

# print(names(monthName))

# ----------------------------------------------


# numbers = (20,27,10,77,49,29,48,99)

# def number(numList):
#     even = 0
#     odd = 10
#     evenlist=()
#     oddlist=()
#     convert1=list(evenlist)
#     convert2=list(oddlist)

#     for num in numList:
#         if num % 2 == 0:
#             even = even + num
#         elif num % 2 == 1:
#             odd = odd - num

#     odd=odd+100
#     convert1.append(even)
#     evenlist = tuple(convert1)        
#     convert2.append(odd)
#     oddlist = tuple(convert2)


#     total = (evenlist, oddlist)
#     return total        


# print("print even number",number(numbers)[0])
# print("print odd number",number(numbers)[1])

#------------------------------------------------------


# names=('Sahil', 'Priya', 'Akshar', 'kushal', 'Akshit', 'Saakshi')
# small = []

# def number(numList):
#     for x in numList:
#         if x[0].isupper():
#             temp = x[0].lower()+ x [1:].upper()    
#             small.append(temp)
#     abc=tuple(small)
#     return abc

# print(number(names))        

#------------------------------------------------------

# tem_celsius=(20,90,45,67,55,70,19)
# tem_fehrenheit=[]

# def temperature(number):

#     for x in number:
#         ver=(x * 9/5) + 32
#         tem_fehrenheit.append(ver)
#     abc=tuple(tem_fehrenheit)
#     return abc    

# print(temperature(tem_celsius)) 

#------------------------------------------------------
# tem_fehrenheit=(20,90,45,67,55,70,19)
# tem_celsius=[]
# def temperature(number):

#     for x in number:
#         ver=(x - 32) * 5/9
#         tem_celsius.append(ver)
#     abc=tuple(tem_celsius)
#     return abc    

# print(temperature(tem_fehrenheit)) 

#------------------------------------------------------

# def numbers(va1, va2):
#     newtuple = ()
#     xyz=list(newtuple)
#     for x in range(0,50,1):

#         if x % va1 == 0 and x % va2 == 0:
#             xyz.append("fizzbuzz")
#         elif x % va1 == 0:
#             xyz.append("buzz")
#         elif x % va2 == 0:
#             xyz.append("fizz")
#         else:
#             xyz.append(x)
#     newtuple=tuple(xyz)
#     return newtuple            


# print(numbers(5,3))
    

#------------------------------------------------------

# number=(78,900,678,75,100,105,450,194)
# def ruppes(cr1):
#     dollars=()
#     xyz=list(dollars) 

#     for amount in number:
#         x= amount * cr1
#         xyz.append(x)
#     dollars= tuple(xyz)
#     return dollars 

# print(ruppes(0.013))       


#------------------------------------------------------

# names=("MANgo", "BANana", "CHErry", "AAPle", "GRApes", "PINepapple")
# def name():
#     small=()
#     xyz=list(small)

#     for x in names:
#         if x[:3].isupper():
#             abc=  x[:3].lower() + x[3:].upper()
#             # print(abc)
#             xyz.append(abc)
#     small=tuple(xyz)
#     return small

# print(name())    

#------------------------------------------------------
#------------------------------------------------------
#------------------------------------------------------

# mixList=("pen", 50 , "book", 100 , 99, True, "paper", 30 , False, 55)
# string=[]
# number=[]
# booleans=[]

# def mixData():

#     for x in mixList:
#         if type(x) == str:
#             string.append(x)
              
#         elif type(x) == int:
#             number.append(x)
                      
#         elif type(x) == bool:
#             booleans.append(x)

#     a1=tuple(string)
#     a2=tuple(number)
#     a3=tuple(booleans)


#     total=(a1,a2,a3)    
#     return total

# result=mixData()

# print(result)    
# print("print string" , result[0])
# print("print integer" , result[1])
# print("print boolean" , result[2])

# print("print string" , mixData()[0])
# print("print integer" , mixData()[1])
# print("print boolean" , mixData()[2])

#------------------------------------------------------

# thistuple = ("apple", "banana", "cherry")

# # This is first way using index and value in tuple
# for i in range(len(thistuple)):
#   print('Element ', thistuple[i])
#   print('Index ', i)

# # This is second way using index and value in tuple
# for index, value in enumerate(thistuple):
#     print('Element ', value)
#     print('Index ', index)

# newList=(2,5,7,1,9,10,55,30,33,89,43,45,12)

# def new():
 
#     result=()
#     xyz=list(result)
#     firstFiveIdx = 0
#     secondFiveIdx = 0
#     remaingIdx = 0
#     lastidx=0
#     for idx, x in enumerate(newList):
#         if idx <= 4:    
#             firstFiveIdx = firstFiveIdx + x 
#         elif idx >= 5 and idx < 10:
#             secondFiveIdx = secondFiveIdx + x
#         elif idx >=10:
#             remaingIdx = remaingIdx + x
#     firstFiveIdx = firstFiveIdx * 2 
#     secondFiveIdx = secondFiveIdx / 2       
            
#     xyz.append(firstFiveIdx)
#     xyz.append(secondFiveIdx) 
#     xyz.append(remaingIdx)
#     lastidx=firstFiveIdx + secondFiveIdx + remaingIdx       
#     xyz.append(lastidx)

#     total=tuple(xyz)

#     return total

# print(new()) 

# newList=(2,5,7,1,9,10,55,30,33,89,43,45,12)

# def new():
#   result=()
#     xyz=list(result)
#     abc=0
#-------------------------------------------------------------------


# names=("maNGO", "banANA", "cheRRY", "apPLE", "graPES", "pinepapPLE")
# def name():
#     list1=()
#     list2=()
#     x1=list(list1)
#     x2=list(list2)

#     for x in names:
#         if len(x) <= 5:
#             x1.append(x)
#         else:
#             x2.append(x) 
#     list1=tuple(x1)
#     list2=tuple(x2)
#     total=(list1,list2)
#     return total
# result = name()

# print(result[0])
# print(result[1])

#-------------------------------------------------------------------


# carname=["audi", "mercides", "mahindra", "tata", "renault", "toyota"]

# def names(cars):
#     indianBrands=()
#     germanBrands=()
#     japanisBrand=()
#     xy1=list(indianBrands)
#     xy2=list(germanBrands)
#     xy3=list(japanisBrand)

#     for x in cars:
    
#         if x == "mahindra" or x == "tata":
#             xy1.append(x)
#         elif x == "audi" or x == "mercides":
#             xy2.append(x)
#         elif x == "renault" or x == "toyota":
#             xy3.append(x) 
     
#     indianBrands=tuple(xy1)
#     germanBrands=tuple(xy2)
#     japanisBrand=tuple(xy3)

#     total=(indianBrands,germanBrands,japanisBrand)
#     return total 

# result = names(carname)    


# print(result[0])
# print(result[1])
# print(result[2])


 #-------------------------------------------------------------------

# def number():
#     tup1=()
#     tup2=()
#     tup3=()
#     x1=list(tup1)
#     x2=list(tup2)
#     x3=list(tup3)


#     for x in range(1,101,1):
#         if x % 2 == 0 and x > 1 and x <= 30:
#             # print("even number",x)
#             x1.append(x)
#         elif x % 2 == 1 and x > 30 and x <= 60:
#             # print("odd number, x")
#             x2.append(x)
#         elif x % 3 == 0 and x > 61 and x <= 101:
#             # print("multiples", x)
#             x3.append(x)

#     tup1=tuple(x1)
#     tup2=tuple(x2)
#     tup3=tuple(x3)

#     total=(tup1,tup2,tup3)
#     return total 
# result=number()    

# print(result[0])
# print(result[1])
# print(result[2])

#--------------------------------------------------------------

# def num():
#     newList=()
#     xyz=list(newList)

#     for x in range(-1,-11,-1):
#         xyz.append(x)
#     newList=tuple(xyz)
#     return newList  

# print(num())

#--------------------------------------------------------------

# numbers=(1, 14, 7, 9, 20, 10, 17, 15, 11, 8)
# def number():
#     squares=()
#     cubes=()
#     x1=list(squares)
#     x2=list(cubes)

#     for x in numbers:
#         if x % 2 == 1:
#             sq = x * x 
#             x1.append(sq)       
#         else:
#             cu = x * x * x
#             x2.append(cu)
        
    
#     squares=tuple(x1)
#     cubes=tuple(x2)
#     total=(squares,cubes)
#     return total
# result = number()    
 
# print(result[0]) 
# print(result[1])          

#--------------------------------------------------------------
            
# def number():
#     n1=()
#     x1=list(n1)
#     newVer=0
#     newcnt=0

#     for x in range(1,11,1):

#         newVer = newVer + x
#         # print(newVer) 
#         # 0=0+1
#         # 1=1+2
#         # 3=3+3
#         newcnt = newcnt + 1
#         # 0=0+1
#         # 1=1+1
#         # 2=2+1
#         # 3=3+1
#         # print(newcnt)
#     new_average = newVer / newcnt   
#     x1.append(new_average)
#     return new_average

# print(number())
    
#--------------------------------------------------------------

# number=(20,15, 10, 5, 25, 30, 50, 45, 20, 35,10)
# def numbersfunction():
#     num=()
#     num1=()
#     xyz=list(num)
#     pqr=list(num1)
#     evenSum=0
#     oddsum=0

#     for idx in range(len(number)):
#         print(idx)

#     for idx, x in enumerate(number):


    # for idx, x in enumerate(number):
    #     if idx % 2 == 0:
    #         evenSum = evenSum + x
    #     elif idx % 2 == 1:
    #         oddsum = oddsum + x


    # xyz.append(evenSum)
    # num=tuple(xyz)
    # pqr.append(oddsum)
    # num1=tuple(pqr)
    # total = (num, num1)
    # return total
# result = numbersfunction()    

# print(result[0])
# print(result[1])    

#--------------------------------------------------------------

# numberInKg=(4,9,6,7,10,1,45,19)
# def pound(val):
#     numberInpound=()
#     xyz=list(numberInpound)
# # 1=2.20462
#     for weight in numberInKg:
#         pound=(weight * val)
#         xyz.append(pound)

#     numberInpound=tuple(xyz) 
#     return numberInpound   

# print(pound(2.205))
        
#-------------------------------------------------------------------


# name=("priya", "sahil", "jaanvi", "keni")

# names=name[0]
# print(names)



# number=(20,15, 10, 5, 25, 30, 50, 45, 20, 35,10)
# def numbersfunction():
#     num=()
#     num1=()
#     xyz=list(num)
#     pqr=list(num1)
#     evenSum=0
#     oddsum=0

#     for i in range(len(number)):
#         names=number[i]
   
#         if names % 2 == 0:
#             evenSum = evenSum + names
            
#         elif names % 2 == 1:
#             oddsum = oddsum + names
           


#     xyz.append(evenSum)
#     num=tuple(xyz)
#     pqr.append(oddsum)
#     num1=tuple(pqr)
#     total = (num, num1)
#     return total
# result = numbersfunction()    

# print(result[0])
# print(result[1])
        