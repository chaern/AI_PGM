def abc(a,b):
    return a+b

print(abc(5,3)) #a = 5, b=3

def abc2(*a):
    hap=0
    for i in a:
        hap += i
    return hap

print(abc2(1,2,3,4,5)) #a = (1,2,3,4,5)
def abc3(**kwargs):
    for k, v in kwargs.items():
        print(k,v)
abc3(name="Alice", age = 30, city = "New York")
    # kwargs = {"name": "Alice", "age":30, "city": "New York"}