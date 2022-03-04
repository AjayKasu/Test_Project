# difference between pass, break and continue..
# pass statement
for i in range(10):
    if i == 5:
        pass # the entire range is display  0 to 10
    print(i, end =' ')
# break statement
for i in range(10):
    if i == 5:
        break # break here and stop the next sequence
    print(i) # the output print next line by next line
number = 0
# we can write in other way
for i in range(10):
    if i == 5:
        break    # break here
    print('Number is ',i)
print('Out of loop')
# continue statement
for i in range(10):
    if i == 5:
        continue # the value of 'i' is break and continue the sequence untill the given input come
    print(i, end=" ") # the output  print on a single line
