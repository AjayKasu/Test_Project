#control statements 
#BREAK STATEMENT
for i in range(10):
    if i == 5:
        break # break here and stop(disappear the 5) the sequence here only and will not print next sequence.
    print(i,end=' ,') 
#PASS STATEMENT 
for i in range(10):
    if i == 5:
        pass# Entire sequence will pass here.
    print('i is',i)
#CONTINUE STATEMENT    
for i in range(10):
    if i == 5:
        continue# stop(disappear the 5) at 5 and continue the next sequence here.
    print('number i is',i)
