# check if every letters of first word is present in next word of the list. 
# If present print yes, else print no

# s = ['app', 'apply']
# op -> yes

# s = ["man", "human", "superman", "flash"] 
# op -> no 

s = ['app', 'apply']
temp = s[0]
d ={}
for i in range(len(temp)):
    if temp[i] not in d:
        d[temp[i]] = 1
    else:
        d[temp[i]] += 1
flag = 0

for i in range(1,len(s)):
    word = s[i]
    for j in range(len(word)):
        if word[j] in d:
            val = d[word[j]]
            print(d)
        else:
            break