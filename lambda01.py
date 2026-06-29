def add(a,b):
    return a + b

#add = lambda a, b: a+b
result = add(5, 3)
print(result) #Output : 8

print(add.__doc__) # Output : None
print(add.__name__) # Output : add