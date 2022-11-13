n = 407
sum = 0

temp = n
while n > 0 :
    digit = temp % 10
    sum += digit ** 3 
    digit //= 10
print(sum)

# if n == sum :
#     print(n,"is an armstrong number")
# else:
#     print(n,"is not an armstrong number")