# #using Temp Variable
# def swap_position(list,pos1,pos2):
#     temp=list[pos1]
#     list[pos1]=list[pos2]
#     list[pos2]=temp
#     return list

# list=[10,20,30,40]
# print('orginal list: ',list)
# pos1,pos2=1,3
# print('after swapping: ',swap_position(list,pos1-1,pos2-1))

# Using Tuple Variable
# def swap_position(list,pos1,pos2):
#     get=list[pos1], list[pos2]
#     #unpacking
#     list[pos2],list[pos1]=get
#     return list

# list=[10,20,30,40]
# pos1,pos2=1,3

# print('Original list: ',list)
# print('Swapped list: ',swap_position(list,pos1-1,pos2-2))


# using Inbuilt list.pop()
# def swap_position(list,pos1,pos2):
#     first=list.pop(pos1)
#     second=list.pop(pos2)

#     list.insert(pos1,second)
#     list.insert(pos2,first)
#     return list

# list=[10,20,30,40]
# pos1,pos2=1,3
# print(swap_position(list,pos1-1,pos2-1))


# 3/ using Enumerate

def swap_position(list,pos1,pos2):
    for i, x in enumerate(list):
        #print(i,x)
       
        if i==pos1:
            elem1=x
        if i==pos2:
            elem2=x          
    list[pos1]=elem2
    list[pos2]=elem1
    return list
list=[10,20,30,40]
pos1,pos2=1,3
print('Swapped list: ',swap_position(list,pos1,pos2))

