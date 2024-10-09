#using Temporary Value
list=[1,2,3,4,5]

# 1/ using Temporary Value
# def swapList(list):
#     temp=list[0]
#     list[0]=list[len(list)-1]
#     list[len(list)-1]=temp
#     return list
# print('orginal list:',list)
# print('updated list: ',swapList(list))


#2/ using tuple variable
# def swapList(list):
#     tuple=list[-1],list[0]
#     list[0],list[-1]=tuple
#     return list
# print(swapList(list))

#3/ using * operand
def swapList(list):
    start,*middle, end=list
    list=[end,*middle, start]
    return list
print('updated list: ',swapList(list))

