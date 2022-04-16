def Union(a,b):
    A = set(a)| set(b)
    return len(A)


a = [1,2,3,4,5]
b = [1,2,3,10]
result = Union(a,b)
print(result)

    
        
