count  = 0

def insertion_sort(arr):
  global count 
  count  = 0
  sort(arr)
  return count

def sort(arr):
    global count
    for j in range(1, len(arr)):
      key = arr[j]      
      i = j - 1
      while i >= 0 and arr[i] > key:           
        arr[i + 1] = arr[i]         
        count += 1  # Compare and swap in the above two lines.
        i -= 1      
      count += 1 # While loop exiting.
      arr[i + 1] = key
      count += 1 # Swap: Assigning key to the arr[i + 1] is a swap operation.
    return arr