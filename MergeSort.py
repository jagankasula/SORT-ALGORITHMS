count = 0

def merge_sort(arr):
    global count
    count  = 0
    sort(arr, 0, len(arr) - 1)
    return count

def sort(arr, l, r): 
    global count   
    if r > l:
      m = (l + r) // 2
      sort(arr, l, m)
      sort(arr, m + 1, r)
      return merge(arr, l, m, r)

def merge(arr, l, m, r):
    global count    
    if arr[m] <= arr[m + 1]:
        count += 1 # Comparision on above line.
        return

    # Not Considering array copy as a swap.
    left = arr[:m]    
    right = arr[m:]

    i = j = 0
    k = 0
    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:        
            arr[k] = left[i]            
            i += 1
        else:                
            arr[k] = right[j]             
            j += 1
        count += 1 # if-else comparision.
        k += 1

    while (i < len(left)):           
        arr[k] = left[i]      
        i += 1
        k += 1

    while (j < len(right)):              
        arr[k] = right[j]        
        j += 1
        k += 1