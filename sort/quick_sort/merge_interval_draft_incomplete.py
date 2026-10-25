ints = [[8,10],[1,3],[15,18],[2,6]]
#Output: [[1,6],[8,10],[15,18]]

# not the best way
# start_vals_lst=[item[0] for item in intervals]
# print(start_vals_lst)

ints.sort(key=lambda x: x[0])
print(ints) #[[1, 3], [2, 6], [8, 10], [15, 18]]

new_lst=[]
i=0
#for i in range(len(ints)-1):
while i<=len(ints)-1: 
    print("i:",i)
    if new_lst[-1][1] < ints[i+1][0]:
        new_lst.append(ints[i])
        print("if lst:",new_lst)
    else:
        new_lst.append([ints[i][0],ints[i+1][1]])
        print("else lst:",new_lst)
        #new_lst.remove(ints[i+1])
        i+=1

    i+=1


print(new_lst)
