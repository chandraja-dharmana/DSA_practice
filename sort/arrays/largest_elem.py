a=[40,20,50,10,30]

#sort and then element at the end 
# time complexity O(n log n)
# ===========================================================

max_elem=a[0]
for i in range(len(a)-1):
    if max_elem<a[i+1]:
        max_elem=a[i+1]
    print(max_elem)

print(max_elem)
# time complexity O(n)