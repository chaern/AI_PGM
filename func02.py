def addMany(*args): 
     #print(type(args))
     result = 0 
     for i in args: 
         result = result + i   # *args에 입력받은 모든 값을 더한다.
     return result 

print(addMany(1,2))
print(addMany(1,2,3,4,5))
print(addMany(1,2,3,4,5,6,7,8,9,10))