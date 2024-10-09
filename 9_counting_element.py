list=[8, 6, 8, 10, 8, 20, 10, 8, 8]
# #using loop
# def count(list,x):
#     count=0
#     for i in list:
#         if i==x:
#             count+=1
#     return count
#
# x=8
# print('{} has occured {} times'.format(x, count(list,x)))

# # using list comprehension
# element=8
# x=[i for i in list if i==element]
# print("the element ", element, "ocurs",len(x),"time")

#using enumerate function

# element=8
# x=[value for key,value in enumerate(list) if value==element]
# print("the element ", element, "ocurs",len(x),"time")

#using count

# def count(list,element):
#     return list.count(element)

# element=8
# print('{} has occured {} times '.format(element,count(list,element)))

#using dictionay

# list= ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
# count_dict={}
# for item in list:
#     if item in count_dict:
#         count_dict[item] +=1
#     else:
#         count_dict[item] = 1

# print(count_dict)

#using counter

from collections import Counter
list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

counter=Counter(list)
print(counter)
