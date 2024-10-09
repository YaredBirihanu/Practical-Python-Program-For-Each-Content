list1=[4,5,6,7,8,9,10,11]
# #Using Slicing Technique 

# def cloning(list1):
#     list2=list1[:]
#     return list2
# list2=cloning(list1)

#2 using extend method

# def cloning(list1):
#     list2=[]
#     list2.extend(list1)
#     return list2

#3 using assingnment operator

# def cloning(list1):
#     list2=list1
#     return list2


#4 using shallow copy

# import copy
# list2=copy.copy(list1)
# print(list2)

#5 using list comprehension

# def cloning(list1):
#     list2=[i for i in list1]
#     return list2

#6 using append method

# def cloning(list1):
#     list2=[]
#     for item in list1:list2.append(item)
#     return list2


#7 using coppy() 1.488 second
# def cloning(list1):
#     list2=[]
#     list2=list1.copy()
#     return list2


#using deep copy

# import copy
# list2=copy.deepcopy(list1)
# print(list2)


#7 using enumerat function
 
#using slice function

list2=list1[slice(len(list1))]
print(list2)

#driver code
# list2=cloning(list1)
# print('orginal list: ',list1)
# print('after cloning: ',list2)
