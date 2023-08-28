# Function : code optimization 

# DRY : 

# decleartion of functions

# def xyz():
#     print("this is a xyz function")
    
# call a function

# xyz()

# xyz()


# xyz()


# perameters
# arguments

# def sumthis(a, b, c):
#     c = a + b + c
#     print(c)

# # arguents
# sumthis(12, 10, 100)

# sumthis(100, 200, 200)



# for i in range(1, 11):
#     print("2 x ", i, "=", 2 * i)

# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# .
# .
# .
# .
# .
# 2 x 10 = 20



# table(50)



# def tablee(n):
#     for i in range(1, 11):
#         print(n, "x ", i, "=", n * i)
        

# tablee(6)

# tablee(90) 

# *args
# **kwargs


# def myinfo(name, age):
#     print("my name is : ", name)
#     print("my age is : ", age)
    
# myinfo(age = 20,name =  "moris")


# default perameters

# def sumthisnw(a = 100, b = 200):
#     c = a + b
#     print(c)

# sumthisnw(1, 2)


# *args
# **kwargs

# *args 


def dothis(*abc):
    print(abc)
    z = 0
    for i in abc:
        z = z + i
    print(z)
    
dothis(10, 20, 100)  
