def expression_validation(input_string):
    openbrac=['(','[','{']
    closebrac=[')',']','}']
    input_expression=[x for x in input_string ]
    if input_expression == []:
        return "No brackets are present"
    validation=[]
    position=0
    for i in range(len(input_expression)):
      if input_expression[i] in openbrac:
        validation.append(input_expression[i])
        position+=1
      elif input_expression[i] in closebrac and validation[-1]== chr(ord(input_expression[i])-1) or validation[-1]== chr(ord(input_expression[i])-2):
        validation.pop()
        position+=1
      
    if len(validation)== 0 :
        return 'valid'
    else:
        return position,'invalid expression' 