# 1/ using if condition

def maximum(a,b):
    if a >=b:
        return f"{a} is the maximum value"
    else:
        return f"{b} is the maximum value"
print(maximum(6,7))

# 2/ using max() function

# a,b=4,5
# print(max(a,b))

#3/ using ternary operator
# a,b=5,6
# print(a if a>= b else b)


#4/ using lambda function
# a,b=5,6
# maximum=lambda a,b: a if a>b else b
# print(f"{maximum(a,b)} is a maximum number")

#5/ using list comprehension
# a,b=8,5
# x=[a if a>b else b]
# print('maximum number is:',x)

#6/ using sort() method

# a,b=7,5
# x=[a,b]
# x.sort()
# print(x[-1])
