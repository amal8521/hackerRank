#string after ood position
s = "PythonString"
outputstring = ''
for i in range(len(s)):
    if(i%2 == 0):
        outputstring = outputstring + s[i]
print("string: ",s)
print("string after odd character: ", outputstring) 