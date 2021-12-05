# number=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
# def numbers():
#     newtuple=()
#     xyz=list(newtuple)
#     for x in range(len(number)):
#         pqr=number[x]
#         if x % 2 == 0:
#             xyz.append(pqr)
#     newtuple=tuple(xyz) 
#     return newtuple          

# print(numbers())          
       

# ----------------------------------------------
# numbers=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
# def checkOddEvenNum():
#     evenList = ()
#     oddList = ()
#     xyz=list(evenList)
#     abc=list(oddList)
#     for val in range(len(numbers)):
#         number=numbers[val]
#         if val % 2 == 0:
#             xyz.append(number)
#         else:
#             abc.append(number)

#     evenList=tuple(xyz)
#     oddList=tuple(abc)
#     total = (evenList,oddList)
#     return total

# total=checkOddEvenNum()            
        
# print("even number",total[0])
# print("odd number",total[1])

# -------------------------------------------

# namesOfMember=("pen", "pencile", "book", "wardrobe","chair", "table","laptop")
# def names(name):
#     removename=[]
#     for i in range(len(namesOfMember)):
#         ver=namesOfMember[i]
#         if i != 0 and i !=2 and i !=4:
#             removename.append(ver)
#     leftname =tuple(removename)
#     return leftname
            
# print(names(namesOfMember))


#------------------------------------------------------
# number=(0,1,2,3,4,5,6,7,8,9,10,121,3,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
# def numbers(va1, va2):
#     newtuple = ()
#     xyz=list(newtuple)
#     for x in range(len(number)):
#         numbers=number[x]
#         if numbers % va1 == 0 and numbers % va2 == 0:
#             xyz.append("fizzbuzz")
#         elif numbers % va1 == 0:
#             xyz.append("buzz")
#         elif numbers % va2 == 0:
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

#     for i in range(len(number)):
#         numbers=number[i]
#         x= numbers * cr1
#         xyz.append(x)
#     dollars= tuple(xyz)
#     return dollars 

# print(ruppes(0.013))       


#------------------------------------------------------

# names=("MANgo", "BANana", "CHErry", "AAPle", "GRApes", "PINepapple")
# def name():
#     small=()
#     xyz=list(small)

#     for x in range(len(names)):
#         num=names[x]
#         if num[:3].isupper():
#             abc=  num[:3].lower() + num[3:].upper()
#             # print(abc)
#             xyz.append(abc)
#     small=tuple(xyz)
#     return small

# print(name())    


#------------------------------------------------------

# mixList=("pen", 50 , "book", 100 , 99, True, "paper", 30 , False, 55)
# string=[]
# number=[]
# booleans=[]

# def mixData():

#     for i in range(len(mixList)):
#         val=mixList[i]
#         if type(val) == str:
#             string.append(val)
              
#         elif type(val) == int:
#             number.append(val)
                      
#         elif type(val) == bool:
#             booleans.append(val)

#     a1=tuple(string)
#     a2=tuple(number)
#     a3=tuple(booleans)


#     total=(a1,a2,a3)    
#     return total

# result=mixData()
   
# print("print string" , result[0])
# print("print integer" , result[1])
# print("print boolean" , result[2])


#------------------------------------------------------

# newList=(2,5,7,1,9,10,55,30,33,89,43,45,12)

# def new():
 
#     result=()
#     xyz=list(result)
#     firstFiveIdx = 0
#     secondFiveIdx = 0
#     remaingIdx = 0
#     lastidx=0
#     for i in range(len(newList)):
#         num=newList[i]
#         if i <= 4:    
#             firstFiveIdx = firstFiveIdx + num
#         elif i >= 5 and num < 10:
#             secondFiveIdx = secondFiveIdx + num
#         elif i >=10:
#             remaingIdx = remaingIdx + num
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

#     for x in range(len(names)):
#         name1=names[x]
#         if len(name1) <= 5:
#             x1.append(name1)
#         else:
#             x2.append(name1) 
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

#     for x in range(len(cars)):
#         name=carname[x]
    
#         if name == "mahindra" or name== "tata":
#             xy1.append(name)
#         elif name == "audi" or name == "mercides":
#             xy2.append(name)
#         elif name == "renault" or name == "toyota":
#             xy3.append(name) 
     
#     indianBrands=tuple(xy1)
#     germanBrands=tuple(xy2)
#     japanisBrand=tuple(xy3)

#     total=(indianBrands,germanBrands,japanisBrand)
#     return total 

# result = names(carname)    


# print(result[0])
# print(result[1])
# print(result[2])


#--------------------------------------------------------------

# numbers=(1, 14, 7, 9, 20, 10, 17, 15, 11, 8)
# def number():
#     squares=()
#     cubes=()
#     x1=list(squares)
#     x2=list(cubes)

#     for x in range(len(numbers)):
#         num=numbers[x]
#         if num % 2 == 1:
#             sq = num * num 
#             x1.append(sq)       
#         else:
#             cu = num * num * num
#             x2.append(cu)
        
    
#     squares=tuple(x1)
#     cubes=tuple(x2)
#     total=(squares,cubes)
#     return total
# result = number()    
 
# print(result[0]) 
# print(result[1])          

#--------------------------------------------------------------
# numbers=(1,2,3,4,5,6,7,8,9,10)            
# def number():
#     n1=()
#     x1=list(n1)
#     newVer=0
#     newcnt=0

#     for x in range(len(numbers)):
#         number=numbers[x]
#         newVer = newVer + number
#         newcnt = newcnt + 1
     
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
        


# person = {
#   "info": {
#       "first": "priya",
#       "last": "patel",
#       "age": 23,
#       "collageInfo": {
#           "name": "vidhya mandir",
#           "degree": "Arch.",
#           "year": 5,
#           "friendInfo": {
#               'name': ['Hinal', 'Niti', 'Kishu'],
#               'location': 'surat'
              
#           }
#       }
#   }
# }
# abc=person.get('info').get("collageInfo").get("friendInfo").get("name")[1]
# print(abc)

# task 1 is Access "Kishu" from name in friendInfo

# accessfriendinfo = person.get('info')
# accessfriendinfo1 = accessfriendinfo.get('collageInfo')
# accessfriendinfo2 = accessfriendinfo1.get('friendInfo')
# accessname = accessfriendinfo2.get('name')
# print(accessname[2])

# result=person.get("info").get("collageInfo").get("friendInfo").get("name")[2]
# print(result)
# Location from friendInfo

# accessfriend = person.get( "info")
# abc= accessfriend.get('collageInfo')
# xyz= abc.get('friendInfo')
# accesslocation = xyz.get('location')
# print(accesslocation)

# degree from collageInfo

# accessdegree = person.get("info")
# accessdegree1 = accessdegree.get("collageInfo")
# degree = accessdegree1.get('degree')
# print(degree)

## 3 Last name from info

# x = person.get("info")
# abc = x.get("last")
# print(abc)



person = {
  "info": {
      "first": "priya",
      "last": "patel",
      "age": 23,
      "collageInfo": {
          "name": "vidhya mandir",
          "degree": "Arch.",
          "year": 5,
          "friendInfo": {
              "info1": [
                  {
                      "name": "sahil",
                      "address": "913 east northside",
                      "city": "fortwarth",
                      "state": "texas",
                      "zipCode": 71602,
                      "temp": [70, 29, 67, 90, 56]
                  },
                    {
                      "name": "akshar",
                      "address": "jokha kamrej",
                      "city": "surat",
                      "state": "gujarat",
                      "zipCode": 394107,
                      "temp": [20, 78, 87, 30, 16]
                  },
                    {
                      "name": "saakshi",
                      "address": "92,bhatha",
                      "city": "surat",
                      "state": "gujrat",
                      "zipCode": 397107,
                      "temp": [90, 9, 47, 99, 96]
                  }
              ]
          }
      }
  }
}
# print(person)
# accessinfo= person.get("info").get("collageInfo").get("friendInfo").get("info1")
# # print(accessinfo)
# for x in accessinfo:

#     if x["city"] == "surat":
#         print("my name is ",x["name"])

#     if x["zipCode"] == 71602:
#         print("my name is ", x["name"],"my address is", x["address"],"and i am live in", x["city"])
#         print("which is located in ", x["state"],"and my zipcode is", x["zipCode"])

# for x in accessinfo:
#         print("my name is ", x["name"],"my address is", x["address"],"and i am live in", x["city"])
#         print("which is located in ", x["state"],"and my zipcode is", x["zipCode"])        