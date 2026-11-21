my_dict = {1:"john", 2:"Ball"}
my_dict = {"name": "jack", "age": 29}

print(my_dict["name"])
print(my_dict.get("age"))

my_dict["age"] = 30
print(my_dict)

my_dict["address"] = "karachi bloct 8 clifton teen talwar"
print(my_dict)

my_dict.pop("age")
print(my_dict)

my_dict.clear()
print(my_dict)