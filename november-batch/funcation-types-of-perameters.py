# Functions: 

# Types of Peramters:
#     1) Postational Perameters
#     2) Keyword Perammeters
#     3) Default Perameters
#     4) Veriable length perameters
#         1) *args
#         2) *kwargs

# def sumthis(x, y, h):
#     print(h)
#     z = x + y + h
#     print(z)
    
    
# sumthis(10, 20, 9)
    
    
# def saveinfo(x, y):
#     print(f"username is {x} and user age is {y}")

    
# saveinfo(y = 20, x = "moris")
    
    
    
# 3) Default Perameters:


# def sumthis(x = 0, y = 0, z = 0):
#     c = x + y + z
#     print(c)
    
# sumthis(12, 2, 3)



# 4) Veriable length perameters
#         1) *args :: arbitrary postional argumets
#         2) **kwargs : keyword arbitrary postional arguments


# def sumthisall(*x):
#     tol = 0 
#     for i in x:
#         tol = tol + i 
#     print(tol)
    
# sumthisall(2, 4, 90, 6)


    
def saveinfo(**qw):
    print(qw)
    
    
saveinfo(name = "kriss", age = 20, number = 9238649323)
    
    