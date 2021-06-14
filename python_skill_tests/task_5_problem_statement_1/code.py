def minJumps(arr):
  if len(arr) <= 1 :
    return 0
  max_element_jump = arr[0]
  no_of_jumps =  arr[0]
  jump =0 
  for position in range(len(arr)):
    if position == len(arr)-1:
      return jump
    if position + arr[position] > max_element_jump:
      max_element_jump = position+arr[position]
    no_of_jumps -= 1 
    if no_of_jumps == 0 :
      jump += 1 
      no_of_jumps = max_element_jump - position
  return jump

