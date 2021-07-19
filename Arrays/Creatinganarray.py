import array as arr
a=arr.array('i',[1,2,3,4])
for i in a:
    print(i)
print(a[2]) # accessing the element at position 2

print(a[-1]) # accessing the elements from backward
print(a[-3])

#Basic Array operations
a.append(5) # appending the array
print(a[4]) # printing the appended value
a.pop() # deletes the number at the end
a.insert(2,10) # inserting the value at the 2nd postion
a.extend([9,22,43]) # adding multiple values at the end of an array
print(a)
