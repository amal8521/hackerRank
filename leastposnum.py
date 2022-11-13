# Finf the missing least positive integer from the list
# [1,-1,3,7,8,0,2,5,-6]
# op -> 4

# [3,7,-1,8,9,10]
# op -> 1

n = 1
flag = 0
l = [3,7,-1,8,9,10]
while n > 0:
    if n in l:
        n += 1
    else:
        flag = 1
        break
        
if flag:
    print(n)
