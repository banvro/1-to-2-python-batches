# list = ordered, allow duplicate values, mutable

# tuple = ordered, allow duplicate values, imutable

# set : unordered, do not allow duplicate values, mutable

# dictionry : ordered, do not allow duplicate values, mutable





# {key : values, key : value.........}

# json



# dit = {"name" : "moris", "age" : 20, "number" : 9283498264}

# print(dit)

# print(type(dit))


# lst = [12, 34, 23, [34, 56, 2, 10], 90, 10]

# print(lst[3][1])

# dit = {
#     "name" : "moris", 
#     "age" : 20, 
#     "number" : 9283498264, 
#     23 : "ashdvasvdjashd"
    
# }

# print(dit["name"])

# print(dit.keys())

# print(dit.values())


# dit = {
#     "name" : "moris", 
#     "age" : 20, 
#     "number" : 9283498264, 
#     23 : "ashdvasvdjashd",
#     "age" : 89
# }

# print(dit)



# dit = {
#     "name" : "moris", 
#     "age" : 20, 
#     "number" : 9283498264, 
# }


# dit["address"] = "this is my address"
# dit["state"] = "Mohali"


# to delete : 

# dit.pop("number")

# print(dit)



# dict = {
#     1 : {
#         "name" : "kriss", 
#         "age" : 12,
#         "number" : {
#             "number1" : 992834833,
#             "number2" : 98236492834
#         }
#     },
#     2 : {
#         "name" : "moris",
#         "age" : 23,
#         "number" : 3874834234
#     }
# }

# print(dict[1]["number"]["number2"])

# print(dict[2]["age"])








# dit = {
#     "name" : "moris", 
#     "age" : 20, 
#     "number" : 9283498264, 
# }


# for i in dit:
#     print(i, dit[i])




a = ("name", "age", "number", "address", "state")

b = ["kriss", 30, 928364923, "this is address", "mohali"]

# {"name" : "kriss", "age" : 30, "number" : 928364923, "state" : "mohali"}



dict = {}

for i in range(len(a)):
    if a[i] == "address":
        continue
    dict[a[i]] = b[i]



print(dict)


# [1, 3, 6, 10, 15, 21]
