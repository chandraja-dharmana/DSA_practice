#str_all = ["interview", "internet", "internal"]
#str_all = ["cat", "dog", "fish"]
str_all = ["apple", "app", "application"]
str1=str_all[0]
str2=str_all[1]
str3=str_all[2]
common_part=[]
for i,j,k in zip(str1,str2,str3):
    if i==j==k:
        common_part.append(i)
        print(i,j,k)
        continue
    else:
        break

pre="".join(common_part)
print(pre)