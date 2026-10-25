##works but not able to write the results back into the original array
# have used two pointers P left to right and Q right to left
#https://www.youtube.com/watch?v=tWCaFVJMUi8


arr = [35,50,15,25,80,20,90,45]
# Sorting in ascending order 
# [15, 20, 25, 35, 45, 50, 80, 90]

def quicksort(arr):

    if len(arr)<=1:
        return

    arr_len=len(arr)
    pivot=arr[0] #first element
    plow=1
    qhigh=arr_len-1
    
    print("plow:",plow)
    print("qhigh:",qhigh)
    while plow<qhigh:
        p_val=arr[plow]
        q_val=arr[qhigh]

        while p_val<pivot and plow<arr_len-1:
            plow+=1
            p_val=arr[plow]
        
        while q_val>pivot and qhigh>=1:
            qhigh-=1
            q_val=arr[qhigh]

        print("plow:",plow)
        print("qhigh:",qhigh)
        if plow<qhigh:
            #p and q did not cross, swap p and q
            arr[plow],arr[qhigh]=arr[qhigh],arr[plow]
            print("no cross arr:",arr)
            plow+=1
            qhigh-=1

    else:
        if len(arr)==2:
            if arr[0]>arr[1]:
                print("did enter")
                arr[0],arr[1]=arr[1],arr[0]
            return
        else:
            #p and q crossed, swap pivot and q
            arr[0],arr[qhigh]=arr[qhigh],arr[0]
            print("crossed arr:",arr)

    pivot_in=qhigh
    left_arr=arr[:pivot_in]
    right_arr=arr[pivot_in+1:]
    print("left_arr:",left_arr)
    print("right_arr:",right_arr)
    quicksort(left_arr)
    quicksort(right_arr)


quicksort(arr)
print(arr)
