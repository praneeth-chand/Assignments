inp = input()
stack = []
op = ["(",")","[","]","{","}"]
stack = [x for x in inp if  x.isalnum() == False and x in op]
stack="".join(stack)
valid_stack=""
for i in range(len(stack)-1):
  for j in range(i+1,len(stack),2):
    if stack[i] == chr(ord(stack[j])-1) or stack[i] == chr(ord(stack[j])-2):
      valid_stack +=  stack[i]
if len(stack) ==2*len(valid_stack):
  print("valid")
else:
  print("invalid")
       
