count = 0

def tim_sort(arr):
   global count
   count = 0
   sort(arr)
   return count

def sort(arr):
  global count
  min_run = 32
  n = len(arr)
  for i in range(0, n, min_run):
    tim_insertion_sort(arr, i, min((i + min_run - 1), n - 1))
    count += 1 # Comparision (min) in the above line.
  size = min_run
  while size < n:
      for start in range(0, n, size * 2):
          mid = start + size - 1
          end = min((start + size * 2 - 1), (n - 1))
          count += 1 # Comparision (min) in the above line
          merged = tim_merge(
              left=arr[start:mid + 1],
              right=arr[mid + 1:end + 1])
          arr[start:start + len(merged)] = merged
      size *= 2
  return arr

def tim_insertion_sort(arr, left=0, right=None):
  global count
  if right is None:
      right = len(arr) - 1
  for i in range(left + 1, right + 1):
      key = arr[i]
      j = i - 1      
      while j >= left and arr[j] > key:         
          arr[j + 1] = arr[j] 
          count += 1 # Comparision and swap on above two line.
          j -= 1
      count += 1 # While loop exit case.          
      arr[j + 1] = key 
      count+= 1 # Swap: Assigning key to the arr[j + 1] is a swap operation.
  return arr, count


def tim_merge(left, right):
  global count
  merged = []
  i = j = 0
  while i < len(left) and j < len(right):
      if left[i] <= right[j]:
          merged.append(left[i])
          i += 1
      else:
          merged.append(right[j])
          j += 1
      count += 1  # if-else comparision, swap.
  merged.extend(left[i:])
  merged.extend(right[j:])
  return merged