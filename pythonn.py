
def numbers(val):
    newlist=[]

    if val % 2 == 0:
        newlist.append(val)
        # print("numbers are", val)
        return "numbers are ", newlist

for x in range(1,21,1):
    print(numbers(x))



#      ------------------------------------

# num = [20,27,10,77,49,29,48,99]

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

#      ------------------------------------

# def names(*name):
#     capitalName=[]
#     for x in name:
#         abc=x[0:2].upper()+ x [2:]
#         capitalName.append(abc)
#     return capitalName

# print(names("priya", "jaanvi", "shreya", "riya"))


#      ------------------------------------


# def names(*name):
#     capitalLastName=[]

#     for x in name:
#         abc = x[0:-1]+ x[-1].upper()
#         capitalLastName.append(abc)
#     return capitalLastName

# print(names("pen", "pencile", "book")) 

# ---------------------------------------------

# def names(*name):
    
#     newlist=[]
#     ver="abc2021"

#     for x in name:
#         abc= "abc2021" + x
#         newlist.append(abc)
#     return newlist

# print(names("jan", "feb", "march", "april", "may"))

# num = [20,27,10,77,49,29,48,99]

# def evennumber(mynum):
#     evennumberlist=[]
#     oddnumberlist=[]
#     even=0
#     odd=10

#     for x in mynum:
#         if x % 2 == 0:
#             even= even * x
#             evennumberlist.append(x)
#         else:
#             odd= odd - x
#             oddnumberlist.append(x)

#         total = [evennumberlist, oddnumberlist]
#         return total

# finalresult= evennumber(num)
# print("print even number", finalresult[0])
# print('Print Odd Subtract', finalresult[1])

                
            
# numbers = [1,2,3,4,5,6,7,8,9,10]

# def subSumFunction(numList):
#     evenSum = 0
#     oddSub = 100

#     for num in numList:
#         if num % 2 == 0:
#             evenSum = evenSum + num
#         else:
#             oddSub = oddSub - num
    
#     total = [evenSum, oddSub]
#     return total

# finalResult = subSumFunction(numbers)
# print('Print Even Sum ', finalResult[0])
# print('Print Odd Subtract', finalResult[1])