def MaximumSum(array):
  for i in range(len(array)-1):
    array[i+1] = max(array[i+1],array[i]+array[i+1])
  return max(array)
array= [-2, -3, 4, -1, -2, 1, 5, -3]
print(MaximumSum(array))