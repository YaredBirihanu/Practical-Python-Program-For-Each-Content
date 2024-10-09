#1/ using in,loop,any(),sort,find(),counter(),try_except_block

# 1/ using in

def find_first_even_number(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    return None

list=[1, 6, 3, 5, 3, 4]
i=7
if i in list:
    print("exist")
else:
    print('not exist')


#2/ using loop
# list=[1, 6, 3, 5, 3, 4]
# for i in list:
#     if(i==4):
#         print('element exists')
    

# 3/ using Count() function
# list=[1, 6, 3, 5, 3, 4]
# exit_count=list.count(15)
# if exit_count > 0:
#     print('yes')
# else:
#     print('no')


# 4/ using find() method

# list=[1, 6, 3, 5, 3, 4]
# Initializing list
# test_list = [10, 15, 20, 7, 46, 2808]

# print("Checking if 15 exists in list")
# x=list(map(str,test_list))
# y="-".join(x)

# if y.find("15") !=-1:
#     print("Yes, 15 exists in list")
# else:
#     print("No, 15 does not exists in list")


#5 / using try/except block
# def element_exists(list,element):
#     try:
#         list.index(element)
#         return True
#     except ValueError:
#         return False
# list=[1,2,3,4,5]

# print(element_exists(list,4))