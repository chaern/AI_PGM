dict1 = {"name": "Alice", "age": 30, "city":"New York"}
dict1 = {"name": "Bob", "age": 25, "city":"Los Angeles"}
#for key in dict1:
#    print(f"{key}: {dict1[key]}")

# for key, value in dict1.items():
#     print(f"{key}: {key}")

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
           print(f"{key}: {value}")

print_kwargs(name="Charlie", age= 35, city = "Chicago")