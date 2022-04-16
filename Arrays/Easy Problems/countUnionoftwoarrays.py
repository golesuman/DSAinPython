def CountUnion(a,b):
    count = len(a) + len(b)
    for i in b:
        if i in a:
            count -= 1
    return count


a = [1,2,3,4]
b= [3,4,5]

result = CountUnion(a,b)
print(result)

    