# Python Data types:
    # 1) List
    # 2) Tuple
    # 3) Set
    # 4) Dictionry
    
    
#  1) List : ordered, allow duplicasy, mutable(changes)
# []

# list is used for stroring multiple data in a single variable. data may or may be hitrogenious.

# lst = [12, 10, 89, 67, 56, 90, 100, 12]

# print(lst)
# print(type(lst))


# ordered:


# lst = [12, 10, "hlo", True, 100.9]

# print(type(lst))

# ordered : 

# []

# print(lst[3])

# print(lst[-2])


# Slicing:
# :

# lst = [12, 10, "hlo", True, 100.9, 23, 34, 2]


# [start : end : increment]

# start = 0
# end = n - 1
# increment = 1

# print(lst[0 : 7 : 2])

# print(lst[2 : ])


# 3) Mutable: (change)


# a = [23, 45 , 23, 10, 8, "hlo"]

# to add new data:

# 1) append()
# 2) insert()

# a.append("car")

# a.insert(1, 10000)

# print(a)


# to delete elements:

# a = [23, 45 , 23, 10, 8, "hlo"]

# 1) pop()
# 2) remove()

# a.pop()

# a.remove(a[-2])
# a.remove(23)

# a.clear()

# print(a)



# lst = []

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lst = []

# for i in range(1, 11):
#     lst.append(i)

# print(lst)


# 1 ------- 50

# x = []
# y = []



# ["2 x 1 = 2", "this", "2 x 2 = 4", "is", "2 x 3 = 6", "bus"]


a = "this is a car "
st = ""

lst  = []

for i in a:
    if i == " ":
        lst.append(st)
        st = ""
    else:
        st = st + i

# print(st)
    
print(lst)







