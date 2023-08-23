# List : collection of multipal data

# a = 10

# []

lst = [12, "hlo", 19.9, 20, 90, 12]
# print(lst)
# list : ordered, allow duplicacy, mutable

# addaiting data
# 1) append()
# 2) insert()

# lst.append("100")

# lst.insert(1, 1000)

# print(lst)

# to remove:

# pop()
# remove()
# lst = [12, "hlo", 20, 19.9, 20, 90, 12]

# lst.pop()
# lst.remove(lst[3])

# print(lst)

# lst.clear()

# print(lst)



# print(lst[1])

# :  => slice operator

# print(lst[1:4])

# print(lst[2 : ])




# Tuple : ordered, allow duplicacy, imutable
# ()

# tpl = (12, "helow", 10.89, 1000)

# print(tpl)
# print(type(tpl))

# print(tpl[0] + tpl[3])


# print(tpl[-3 : ])

# tpl = (12, "helow", 10.89, 1000)
# print(tpl)
# lst = list(tpl)

# print(lst)

# lst.append(3000)

# print(lst)

# tpl = tuple(lst)

# print(tpl)


# a = 10

# b = str(a)

# print(b, type(b))


# set Unordered, do not allow duplicasy, mutable
# {}


# st = {12, 100, "hlo", "ok", 100}

# print(st)
# print(type(st))

# st.add(100000)

# print(st)

# st.pop()
# st.remove("ok")
# print(st)

# dictionry : mutable, do not allow duplycasy, orders
# {} =>  key : value   pairs


dix = {"name" : "moris",  
        "age" : 30,
        "gender" : "male"
}

print(dix.values())

# print(dix)
# print(type(dix))

# json

# print(dix['age'])

# dix['marks'] = 90

# print(dix)


# dix.pop('age')

# print(dix)



# a = (12, 23, 3,4 , 10)

# for i in dix:
#     print(i)


lst = ["name", "age", "gender", "marks"]

tpl = ("kriss", 20, "male", 90)

dic = {}
print(dic)

dic["io"] = 120

print(dic)

# for i in range(4):
#     x = lst[i]
#     y = tpl[i]
    
#     dic[x] = y
    
# print(dic)


# dic = {}
# output

# {"name" : "kriss", "age" : 20, "gender" : "male", "marks" : 90}






