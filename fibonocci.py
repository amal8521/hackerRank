# n = 5
# a = 0
# b = 1
# if n < 0:
#     print("incorrect output")
# elif(n == 0):
#     print(0)
# elif(n == 1):
#     print(1)
# else:
#     print(0)
#     print(1)    
#     for i in range(1,n):
#         c = a + b
#         a = b
#         b = c
#         print(c)


def fibonacci():
    # return a list of fibonacci numbers
    l = [0,1]
    for i in range(2,5):
        l.append(l[i-2] + l[i-1])
    print(l) 

print(fibonacci(5))

